from flask import Flask,render_template,request,redirect
from src.data_science_project.utils.common import read_yaml
from pathlib import Path
import numpy as np
from src.data_science_project.pipeline.model_prediction_pipeline import Prediction

app=Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/submit")
def submit():
    if request.method=="POST":
        fixed_acidity=float(request.form["fixed acidity"])
        volatile_acidity=float(request.form["volatile acidity"])
        citric_acid=float(request.form["citric acid"])
        residual_sugar=float(request.form["residual sugar"])
        chlorides=float(request.form["chlorides"])
        free_sulfur_dioxide=float(request.form["free sulfur dioxide"])
        total_sulfur_dioxide=float(request.form["total sulfur dioxide"])
        density=float(request.form["density"])
        pH=float(request.form["pH"])
        sulphates=float(request.form["sulphates"])
        alcohol=float(request.form["alcohol"])

        data=[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,
              density,
              pH,
              sulphates,
              alcohol]
        
        data=np.array(data)
        data=data.reshape(1,-1)

        predict=Prediction()
        result=predict.predict(data)


        
    return f"{int(np.round(result)[0])}"


if __name__=="__main__":
    app.run(debug=True)