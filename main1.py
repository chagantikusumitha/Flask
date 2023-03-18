#step-1 : import Flask( flask is module Flask is class)
from flask import Flask,request

#step-2 : app is the object we are creating for Flask class with the parameter __name__
app=Flask(__name__)

#step 3 : create an endpoint using route and bind them with a functionality
@app.route('/')
def home_page():
    return " Welcome to home page "

@app.route('/search')
def search_page():
    return " welcome to search page "

@app.route('/findme')
def findme_page():
    return "   chagantikusumitha : https://www.linkedin.com/in/chagantikusumitha/ "

@app.route('/upper')
def upper_case():
    a=request.args.get('a')
    return str(a).upper()

@app.route('/lower')
def lower_case():
    a=request.args.get('a')
    return str(a).lower()

@app.route('/add')
def add_sum():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+int(b))

@app.route('/div')
def div_sum():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)/int(b))

@app.route('/sub')
def add_sub():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)-int(b))

@app.route('/multi')
def add_multi():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)*int(b))

#step=4 : run the app
if __name__=='__main__':
    app.run(debug=True)