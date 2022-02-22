from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/submit')
def submit():
        result=""
        input = request.args.get('number','Nothing')
        if(input==''):
            result='No number Provided!'
        elif((input.isdigit())):
            if((int(input)) %2 == 0):
                result = ' is even'
            elif((int(input)) %2 != 0):
                result = ' is odd'
        else:
            result = ' is not an integer or is Decimal!'
        return render_template('submit.html',input=input,result=result)
