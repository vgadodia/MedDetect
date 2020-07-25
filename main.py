#!/bin/env python
from app import create_app, socketio

main_app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(main_app)
