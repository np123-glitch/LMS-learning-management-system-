from flask import Blueprint, render_template, request, jsonify
import sys
import json


views = Blueprint(__name__, "views")

@views.route("/")
def home():
        return render_template("home.html")
        
@views.route("/signup", methods=['POST', 'GET'])
def signup():
        if request.method == 'POST':
                data = {'studentname' : request.form.get("studentname"),
                'parentname' : request.form.get("parentfirstname"),
                'email' : request.form.get("email")}
                json_obj = json.dumps(data)
                with open("students.txt", 'a') as f:
                        f.write(json_obj)
                        f.write("\n")
                return render_template("redirect.html")
        return render_template("createanaccount.html")
@views.route("/dashboard", methods=["POST", "GET"])
def dashboard():
        
        return render_template("dashboard.html", data=request.form.get("uname"))


@views.route("/test", methods=["POST", "GET"])
def test():
        action = request.form.get("action")
        
        studentrecord = {}
        if action == "r":
                
                data = request.form.get("data")
                studentid = json.loads(data)["id"]
                
                json_obj = None
                with open('C:/Users/sachi/coding/studentinfo.json') as file:
                        json_obj = json.loads(file.read())
                
                        studentArr = json_obj["students"]
                       
                        for i in studentArr:
                                if i["id"] == studentid:
                                        studentrecord = i
        elif action == "w":
                
                data = request.form.get("data")
                studentid = json.loads(data)["id"]
                
                json_obj = ""
                with open('C:/Users/sachi/coding/studentinfo.json', 'r+') as file:
                        json_obj = json.loads(file.read())
                        
                        studentArr = json_obj["students"]
                        for i in studentArr:
                                if i["id"] == studentid:
                                        i["fees"] = json.loads(data)["fees"]
                                        studentrecord = i
                                        file.seek(0)
                                        json.dump(json_obj, file)
                                        file.truncate()
                                        
                                        break
        else:
                return "NOT VALID ACTION"
        
        return '{"id":' + ' "' + studentrecord["id"] + '",'  + '"studentname":' + ' "' + studentrecord["studentname"]  + '",' + '"fees":' + ' "' + studentrecord["fees"] + '"}'

@views.route("/login", methods=["POST", "GET"])
def login():
        print(request.form.get("uname"), file=sys.stderr)
        return render_template("login.html")
@views.route("/book", methods=["POST", "GET"])
def book():
        return render_template("signin.html")
        

        

