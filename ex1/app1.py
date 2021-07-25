#flask basic program for multiple routes
'''routes- they are just used to call the webpages  
which we are given in the functions'''
'''if we execute this program we get url-http://127.0.0.1:5000/
we should paste this url in browser
'''

from flask import Flask
app=Flask(__name__)

'''here ('/') - it's a default web page which will return the index 
function return value'''
@app.route('/')
def index():
    return "<h1>Hellow world bla bla <br>  <p>hellow</p></h1>"

'''here to access the home function then we should  write the /home at the end as
http://127.0.0.1:5000/home '''

@app.route('/home')
def home():
    return "this is home page"

'''here to access the about function then we should  write the /about at the end as
http://127.0.0.1:5000/about '''
@app.route('/about')
def about():
    return "this is about page"

if __name__=="__main__":
    app.run()

#we will learn managing routes later excercises here we are acessing them manually