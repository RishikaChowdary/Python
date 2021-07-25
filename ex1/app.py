#simple hellow world on web page
from flask import Flask
#here we are importing Flask class from flask module

app=Flask(__name__)

#app is a object of Flask

# @app.route()- it's a decorator in python which adds extra features to the function

@app.route('/')
def index():
    return "Hellow world"

# it's a starting web app here we are just print hellow world on the web page


#main method in python
if __name__=="__main__":

    app.run()


#  app.run() is used to run the localhost() server in the system
