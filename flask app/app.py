# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:58:32 2022

@author: Vishnuvardhana chary
"""

from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
model=pickle.load(open('cerealanalysis.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template("base.html")

@app.route('/assesment')
def prediction():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def admin():
    a=request.form["mfr"]
    if (a=='a'):
        a1,a2,a3,a4,a5,a6,a7=1,0,0,0,0,0,0
    if (a=='g'):
        a1,a2,a3,a4,a5,a6,a7=0,1,0,0,0,0,0
    if (a=='k'):
        a1,a2,a3,a4,a5,a6,a7=0,0,1,0,0,0,0
    if (a=='n'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,1,0,0,0
    if (a=='p'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,1,0,0
    if (a=='q'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,1,0
    if (a=='r'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,0,1
    
    b=request.form["type"]
    if(b=='c'):
        b=0
    if(b=='h'):
         b=1
    c=request.form["calories"]
    d=request.form["protein"]
    e=request.form["fat"]
    f=request.form["sodium"]
    g=request.form["fiber"]
    h=request.form["carbo"]
    i=request.form["sugars"]
    j=request.form["potass"]
    k=request.form["vitamins"]
    l=request.form["shelf"]
    m=request.form["weight"]
    n=request.form["cups"]
     
    t=[[int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i),int(j),int(k),int(l),int(m),int(n)]]
    y=model.predict(t)
    print(y)
    return render_template("prediction.html",z=y[0][0])

if __name__ == '__main__':
    app.run(debug=False)   











