from flask import Flask,render_template,request

app=Flask(__name__)

import numpy as np
import pandas as pd
import pickle

File_Open=open('Car_Price.pkl','rb')
Model=pickle.load(File_Open)

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Predict",methods = ["GET", "POST"])
def Predict():
    if request.method == "POST":

        Year_Bought=int(request.form["year"])
        Number_Year=(2020-Year_Bought)

        Present_Price=float(request.form["price"])

        Owner=int(request.form["owner"])

        Kms_Driven=int(request.form["km"])

        Transmission=request.form["transmission"]
        if Transmission=='Manual':
            Transmission_Manual=1
        else:
            Transmission_Manual=0

        Seller_Type=request.form["seller"]
        if Seller_Type=='Individual':
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0

        Fuel_Type=request.form["fuel"]
        if Fuel_Type=='Diesel':
            Fuel_Type_Diesel=1
            Fuel_Type_Petrol=0

        elif Fuel_Type=='Petrol':
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=1

        else:
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=0

        Prediction=Model.predict([[Present_Price, Kms_Driven, Owner, Number_Year,
        Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,
        Transmission_Manual]])

        Output=round(Prediction[0],2)
        return render_template('Result.html',prediction_text="{}".format(Output))
    return render_template("Index.html")



if __name__=='__main__':
    app.run(debug=True)
