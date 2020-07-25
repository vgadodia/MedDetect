from flask import session, redirect, url_for, render_template, request

from .forms import LoginForm
from flask import Flask, jsonify, request, send_file, render_template, redirect, url_for, make_response
from flask_socketio import SocketIO, send
import numpy as np
from . import main
import matplotlib.pyplot as plt
import tensorflow.keras
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import pathlib
import hashlib

from PIL import Image, ImageOps

np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model('keras_model.h5')

import pyrebase

config = {
  "apiKey": "AIzaSyBs6Byg5HK_dlFOSIcmcjsjEyI8zceppYM",
  "authDomain": "med-detect.firebaseapp.com",
  "databaseURL": "https://med-detect.firebaseio.com",
  "storageBucket": "med-detect.appspot.com"
}

firebase = pyrebase.initialize_app(config)


db = firebase.database()
def add_patient(k):
    db.push({"date":k[0], "firstname":k[1], "lastname":k[2], "age":k[3], "height":k[4], "weight":k[5], "diagnosis":k[6], "prob":k[7]})

def get_patients():
    x = db.get().val()
    final = []
    for i in x:
        final.insert(0, [x[i]['date'], x[i]['firstname'], x[i]['lastname'], x[i]['age'], x[i]['height'], x[i]['weight'], x[i]['diagnosis'], x[i]['prob']])
    return final

def get_numbers():
    a = 0
    b = 0

    for i in get_patients():
        if i[6] == "Uninfected":
            a += 1
        else:
            b += 1
    return [a, b]
def get_age_data():
    k = get_patients()
    final = [0, 0, 0, 0, 0]

    for i in k:
        if i[6] == "Parasitized":
            if int(i[3]) < 20:
                final[0] += 1
            elif int(i[3]) >= 20 and int(i[3]) < 40:
                final[1] += 1
            elif int(i[3]) >= 40 and int(i[3]) < 60:
                final[2] += 1
            elif int(i[3]) >= 60 and int(i[3]) < 80:
                final[3] += 1
            else:
                final[4] += 1
    return final
@main.route('/forum', methods=['GET', 'POST'])
def index2():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index2.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)

@main.route('/')
def index():
    # print(predict('input1.jpg'))
    return render_template('index.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')

@main.route('/trends')
def trends():
    k = get_numbers()
    k1 = get_age_data()
    return render_template('trends.html', a = k[0], b = k[1], p = k1[0], q = k1[1], r = k1[2], s = k1[3], t = k1[4])


@main.route('/download', methods=["GET", "POST"])
def download():
    return redirect("/portfolio")

@main.route('/upload', methods=['GET', 'POST'])
def getupload():
    if request.method == "POST":
        try:
            memory = request.files['memory']
            
            if memory.filename != "":
                memory.save(memory.filename)
                data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
                image = Image.open(memory.filename)
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.ANTIALIAS)
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                prediction = model.predict(data)
                
                result = prediction[0]
                # print(result)
                diagnosis = ""
                prob = 0
                if result[0] > result[1]:
                    diagnosis="Uninfected"
                    prob = round(result[0] * 100, 2)
                else:
                    diagnosis = "Parasitized"
                    prob = round(result[1] * 100, 2)
                text = "hello there"

                firstname = request.form["firstname"]
                lastname = request.form["lastname"]
                age = request.form["age"]
                height = request.form["height"]
                weight = request.form["weight"]
                now = datetime.now()
                date = now.strftime("%d/%m/%Y %H:%M:%S")
                new_entry = [date, firstname, lastname, age, height, weight, diagnosis, str(prob)]
                add_patient(new_entry)
                
                
                return render_template('results.html', diagnosis=diagnosis, prob=prob, result=result, text=text)
            
            else:
                return render_template('upload.html', errorMessage="Please upload either a jpeg or png image.")
        except:
            print("EXCEPT")
            return render_template('upload.html', errorMessage="Please upload either a jpeg or png image.")
    return redirect("/upload")

@main.route('/stats')
def stats():
    return render_template('stats.html')

@main.route('/portfolio')
def help():
    
    return render_template('portfolio.html', entries=get_patients())

@main.route('/404')
def error():
    return render_template('404.html')