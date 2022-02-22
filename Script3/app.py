from flask import Flask, render_template,request

app = Flask(__name__)


dict={}

@app.route('/')
def home():
    return render_template('home.html')

@app.route ('/submit' ,methods=['POST','GET'])
def register():
    name = request.form.get('name',)

    organization = request.form.get('organization',)
    if(request.method == 'POST'):
        dict[name]=organization
    return render_template('submit.html', dict=dict,)