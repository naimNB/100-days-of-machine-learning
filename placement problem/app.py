from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    cgpa = float(request.form["cgpa"])
    iq = float(request.form["iq"])

    features = np.array([[cgpa, iq]])
    prediction = model.predict(features)[0]

    result = "Placed" if prediction == 1 else "Not Placed"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)