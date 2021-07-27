# -*- coding: utf-8 -*
"""Spyder Editor

This is a temporary script""" 
#importing libraries
import numpy as np
import pandas as pd
from flask import Flask,request,render_template
import pickle
#initailize the flask
app = Flask(__name__,template_folder='templates')

cat_boost= pickle.load(open('model1.pkl','rb'))

#Define html file to get user input
@app.route('/',methods=['GET'])
def home():
    return render_template('Khushi Prediction1.html')

@app.route('/predict',methods=['POST'])
def predict():
    City_Name =request.form.get('City_Name')
    BHKS = request.form.get('BHKS')
   # Area = request.form.get('Area')
    build_up_area = request.form.get('build_up_area')
    Housetype= request.form.get('Housetype')
    Location = request.form.get('Location')
    deposit = request.form.get('deposit')
    sqft_per_inch=request.form.get('sqft_per_inch')
    BHKS = float(BHKS)
    deposit = str(deposit)
    #Area = float(Area) 
    #area_sqft = int(area_sqft)
    #area_sqft = np.log(area_sqft)
    print(City_Name)
    print(BHKS)
   # print(Area)
    print(build_up_area)
    print(Housetype)
    print(Location)
    print(deposit)
   

    predictions = cat_boost.predict([[City_Name,BHKS,sqft_per_inch,build_up_area,Housetype,Location,deposit]])
    
    predictions = np.exp(predictions)
    

    prediction_text = 'House rent is predicted to be :  '+str(predictions)


    return render_template('Khushi Prediction1.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
