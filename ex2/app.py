# Accessing html files in flask

from flask import Flask, render_template

#here we are importing Flask class and render_templete

#render_templete is used to return the html files

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run()

