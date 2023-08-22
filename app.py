import smtplib
import json
from flask import Flask, render_template, request, jsonify
from chat import get_response
app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    str=json.dumps(text)

    #TODO: CHECK IF TEXT IS VALID
    response=get_response(text)
    #print(response)
    if response[:8] == "[Alert!]":
        response=response[8:]
        s = smtplib.SMTP('smtp.gmail.com', 587)
 
        # start TLS for security
        s.starttls()
 
        # Authentication
        s.login("tomtexting4@gmail.com", "ietpbkwjkjhwfnzw")
 
        # sending the mail
        s.sendmail("tomtexting4@gmail.com", "userparent123@gmail.com", str)

        # terminating the session
        s.quit()
        
    message={"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)