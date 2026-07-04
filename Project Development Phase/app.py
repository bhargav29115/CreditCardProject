from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("best_creditcard_model.pkl")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    data = []

    data.append(float(request.form["Time"]))
    data.append(float(request.form["V1"]))
    data.append(float(request.form["V2"]))
    data.append(float(request.form["V3"]))
    data.append(float(request.form["V4"]))
    data.append(float(request.form["V5"]))
    data.append(float(request.form["V6"]))
    data.append(float(request.form["V7"]))
    data.append(float(request.form["V8"]))
    data.append(float(request.form["V9"]))
    data.append(float(request.form["V10"]))
    data.append(float(request.form["V11"]))
    data.append(float(request.form["V12"]))
    data.append(float(request.form["V13"]))
    data.append(float(request.form["V14"]))
    data.append(float(request.form["V15"]))
    data.append(float(request.form["V16"]))
    data.append(float(request.form["V17"]))
    data.append(float(request.form["V18"]))
    data.append(float(request.form["V19"]))
    data.append(float(request.form["V20"]))
    data.append(float(request.form["V21"]))
    data.append(float(request.form["V22"]))
    data.append(float(request.form["V23"]))
    data.append(float(request.form["V24"]))
    data.append(float(request.form["V25"]))
    data.append(float(request.form["V26"]))
    data.append(float(request.form["V27"]))
    data.append(float(request.form["V28"]))
    data.append(float(request.form["Amount"]))

    prediction = model.predict([data])

    if prediction[0] == 1:
        result = "Fraud Transaction Detected"
    else:
        result = "Normal Transaction"

    return render_template("result.html", prediction=result)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)