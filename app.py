from flask import Flask,render_template,session,request,redirect
from flask_socketio import join_room,leave_room,SocketIO,send
from string import ascii_uppercase
import random

# init flask app
app=Flask(__name__)
# config flask app
app.config["SECRET_KEY"] = "loremlorem"
socketio=SocketIO(app)

@app.route("/",methods=["POST","GET"])
def home():
    return render_template("home.html")

if( __name__ == "__main__"):
    socketio.run(app,debug=True)
