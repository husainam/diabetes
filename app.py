from flask import Flask, request, redirect, render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("Diabetes.pkl", "rb"))
model1 = pickle.load(open("model1.pkl", "rb"))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/sugar')
def sugar():
    return render_template("sugar.html")


@app.route('/cardio')
def cardio():
    return render_template("cardio.html")


@app.route('/cardiopredict', methods=['POST', 'GET'])
def results():
    text1 = request.form['1']
    text2 = request.form['2']
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
    text9 = request.form['9']
    text10 = request.form['10']
    text11 = request.form['11']
    text12 = request.form['12']

    row_df = pd.DataFrame(
        [pd.Series([text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12])])

    prediction = model1.predict_proba(row_df)

    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    output = float(output)*100
    if output > 50.0:
        return render_template('result3.html', pred=f'You have chance of having CVD.\nProbability of having CVD is {str(output)} %')
    else:
        return render_template('result2.html', pred=f'You are safe.\n Probability of having CVD is {str(output)} %')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    text1 = request.form['1']
    text2 = request.form['2']
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']

    row_df = pd.DataFrame(
        [pd.Series([text1, text2, text3, text4, text5, text6, text7, text8])])

    prediction = model.predict_proba(row_df)

    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    output = float(output)*100
    if output > 50.0:
        return render_template('result1.html', pred=f'You have chance of having diabetes.\nProbability of having Diabetes is {str(output)} %')
    else:
        return render_template('result2.html', pred=f'You are safe.\n Probability of having diabetes is {str(output)} %')


if __name__ == '__main__':
    app.run(debug=True)
