
## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for,jsonify

## create the flask app

app=Flask(__name__)

@app.route('/',methods=['GET']) #Routing takes 2 parameters [Starting Url , Method]
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome',methods=['GET'])
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

## Variable Rule
#@app.route('/success/<score>')  # default method will be the get method
#def success(score):
#    return "The person has passed and the score is: "+ score

@app.route('/success/<int:score>') # default method will be the get method
def success(score):
    return "the person is passed and the score is "+str(score)

@app.route('/fail/<int:score>') # default method will be the get method
def fail(score):
    return "the person has failed and the score is "+str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3
        result="" 
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)
    
## Create API AND Test It On Postman
#test this jsone In Postman 
# {
#    "a":10,
#    "b":20
#}

@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)

# Without Using Any Frontend We can Test Our Result Using API Like This





if __name__=='__main__':  #__name__ is the starting point of the app or code
    app.run(debug=True)