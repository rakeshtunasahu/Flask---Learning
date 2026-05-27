#now this will show how the HTTP methods work in flask

from flask import Flask, request

HTTP= Flask(__name__)

@HTTP.route("/submit" , methods=["Get", "POST"])
def submit():
    if request.method == "POST":
        return "Form submitted successfully"
    else:
        return "Please submit the form using POST method"



