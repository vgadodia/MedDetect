# MalariaDiagnosis
A machine learning disease detection and user management system for hospitals and medical clinics to instantly diagnose diseases such as malaria from blood samples, with high accuracy.

### Features work best when run locally. In order to do this, `cd` into the project directory, and do `flask run`.

## Inspiration
According to the WHO, malaria is among the top 10 deadliest diseases in low income nations, causing over 405,000 deaths worldwide in 2018 alone. The major cause of this is lack of infrastructure and human resource required to treat this disease. We believe that machine learning can be used to combat this global issue and improve the efficiency of the healthcare system, and reduce the dependence on human resources.

## What it does
Med Detect is a machine learning automatic disease detection and user management system targetted towards hospitals and medical clinics, that enables them to instantly diagnose diseases such as malaria from blood samples, with a high accuracy. Our system collects basic information and an image, and then returns quick and accurate results. We use advanced machine learning algorithms to classify the user uploaded image into uninfected (normal) or parasitized (diagnosed with malaria), and then automatically generate a CSV medical report. We also have a patient data management system, as well as a data visualisation page, displaying various analytics regarding patients.

Med Check significantly reduces the human resource and expertise required for diagnosing malaria and makes the entire system far more efficient and less prone to error. Med Check would have a huge impact in rural areas in nations like India, where there is acute lack of qualified doctors to detect such diseases.

## How we built it
* Python flask for the web app and HTML/CSS/js templates for the front-end.
* Flask socket-io for the forums page.
* Keras with TensorFlow back-end for the image classification model.
* Google Firebase for storing patient data.
* Google charts for data visualization.
* AWS for web hosting

## Challenges we ran into
The first major challenge we ran into was getting good quality training data for the ML model. After hours of research, we were able to compile a dataset that allowed us to provide fast and accurate classifications. As it was our first time with firebase, we also struggled with integrating fire-base to store patient data. With minimal prior experience with chat functionalities, getting the forums page to work seamlessly with socket-io was another big challenge. Lastly, hosting web applications with data intensive ML models such as this one was a huge hurdle, which we tried our best to approach using Amazon Web Services.

## Accomplishments that we're proud of
We are proud to have developed a relatively fast and efficient model to predict with over 90% accuracy on the test dataset. We are also proud to have learned firebase in a relatively short amount of time, and to have integrated it with a fully functional firebase database connected to our web app. Lastly, we are proud to have created a feature-rich web app and clean UI within the time constraint.

## What we learned
We learned how to use tensorflow and keras for image classification. We also learned how to use web sockets and socket-io in order to create realtime chats through which multiple people can communicate from different windows. Lastly, we learned for the first time how to set up a firebase database and integrate it with a flask web-app.

## What's next for Med Detect
We hope to develop a login system for specific hospitals to access their patients' data securely. We also want to male a more sophisticated forums page and data visualization page, to help provide more detailed analytics. We anticipate getting a domain name for the web app, as well as expanding to a mobile app. Lastly, we hope to experiment with more robust front-end frameworks such as React.
