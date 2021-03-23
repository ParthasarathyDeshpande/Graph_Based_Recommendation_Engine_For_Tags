# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:16:42 2020


"""
''' I uesd the flask for creating the web application'''
from flask import Flask, request, render_template
import pickle

'''app will be the name of app that we will be giving with writing Procfile'''

app = Flask(__name__)
model = pickle.load(open('graph.pkl', 'rb'))

'''theis will be home page of the web application'''
@app.route('/')
def home():
    return render_template('index.html')


'''this will be the page where recommended tags'''

@app.route('/recommend',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        prediction = list(dict(sorted(dict(model[request.form['Tag']]).items(),
                                  key = lambda x: x[1]['weight'], reverse = True)).keys())
        return render_template('index.html', prediction_text=str(prediction))
    except KeyError:
        return render_template('index.html', prediction_text = 'Sorry "' + request.form['Tag'] + '" key does not exist. Please enter a valid key.')


if __name__ == "__main__":
    app.run(debug=True)
