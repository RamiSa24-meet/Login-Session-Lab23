from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


	
@app.route('/',methods=['GET', 'POST'])  # '/' for the default page
def login():
  if request.method == 'GET':
    return render_template('home.html')
  else:
    try:
      z =request.form['Number'] 
      x = request.form['Name']
      y = request.form['Quote']
      login_session['Age']= z
      login_session['Quote']=y 
      login_session['Name']= x
      return render_template('thanks.html',login_session = login_session)
    except:
       return render_template('error.html')

    
	      


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	return render_template('display.html',login_session = login_session ) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)