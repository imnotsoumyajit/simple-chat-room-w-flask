from flask import Flask,render_template,session,request,redirect,url_for
from flask_socketio import join_room,leave_room,SocketIO,send
from string import ascii_uppercase
import random

# init flask app
app=Flask(__name__)
# config flask app
app.config["SECRET_KEY"] = "loremlorem"
socketio=SocketIO(app)

# rooms is a dictionary
rooms={}
# gen a unique code 
def generate_unique_code(length):
    while True:
        code = ""
        # _ is an anonymous variable
        for _ in range(length):
            code+=random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code




@app.route("/",methods=["POST","GET"])
def home():
    session.clear() 
    if request.method == "POST":
        # this form object is a dictionaryv
        name=request.form.get("name")
        code=request.form.get("code")
        join=request.form.get("join",False)
        create=request.form.get("create",False)

        # if the user did not pass a name
        if not name:
            return render_template("home.html",error="Enter a name dumbass",code=code,name=name)
            # ,code=code,name=name is given as the window refreshes and we have to provide them back the details
        # if the user is trying to join the room
        if join != False and not code:
            return render_template("home.html",error="Enter a room code..loner",code=code,name=name)

        # what room this user will be going into and check if it exists,if not we generate a room for them
        room == code
        if create!=False:
            room=generate_unique_code(4)
            rooms[room] = {"memebers":0,"messages":[]}

        # If the room do not exists
        elif code not in rooms:
            return render_template("home.html",error="The room seems not to exist",code=code,name=name)


        # as session is a temp way to store data about a user   
        session[room]=room
        session[name]=name
        # redirect user to new page (chat room)
        return redirect(url_for("room")) 

    # ,code=code,name=name not needed in this as they are only for post requests
    return render_template("home.html")

@app.route("/room")
def room():
    return render_template("room.html")

if( __name__ == "__main__"):
    socketio.run(app,debug=True)
