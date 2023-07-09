from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))






cols = ['caste','rank','gender']

casteMap = {
    'oc':0,
    'bc-a':1,
    'bc-b':2,
    'bc-c':3,
    'bc-d':4,
    'bc-e':5,
    'sc':6,
    'st':7,
}

genderMap = {
    'male':0,
    'female':1
}

branchMap = {
    0:'cse (computer science engineering)',
    1:'ece (electronics and communciation engineering)',
    2:'eee (electrical and electronics engineering)',
    3:'ce (civil engineering)',
    4:'me (mechanical engineering)'
}

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    global cols
    if request.method == 'GET':
        return render_template('base.html', columns=cols)

@app.route('/predict', methods=['POST', 'GET'])
def pred():
    global cols,casteMap,genderMap,branchMap
    if request.method == 'POST':
        caste = request.form['caste']
        rank = request.form['rank']
        gender = request.form['gender']
        input_arr = np.array([casteMap[caste],rank,genderMap[gender]]).reshape(1,-1)
        prediction = model.predict(input_arr)
        prediction = prediction[0]
        pred = branchMap[prediction]
        return render_template('result.html', result=pred)
    else:
        return render_template('base.html',columns=cols)

if __name__ == '__main__':
    app.run(debug=True)