from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
 
  "apiKey": "AIzaSyCgZRbd5dXKkyyz8oSOjzw72mI9SCrnXvg",

  "authDomain": "try-firebase-14760.firebaseapp.com",

  "projectId": "try-firebase-14760",

  "storageBucket": "try-firebase-14760.appspot.com",

  "messagingSenderId": "380736490668",

  "appId": "1:380736490668:web:394254281c9ea4dd602309",

  "measurementId": "G-ZM4HSTG39N",
    "databaseURL":"https://try-firebase-14760-default-rtdb.europe-west1.firebasedatabase.app/"
  }


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()    

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('add_tweet'))
    except:
        return render_template("signup.html")

    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('add_tweet'))
    except:
        return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)