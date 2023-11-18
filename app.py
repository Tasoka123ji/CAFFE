from flask import Flask,render_template,request
from person import User
import sqlite3

app = Flask(__name__)
    
@app.route('/sing_up')
def hello_world():
    return render_template('sing_up.html')

@app.route('/sing_up',methods = ["POST"])
def sing_up():
    if request.method == "POST":
        person = request.form
        user = User(name=person['name'], email=person['email'],
                    phone_number=person['phone_number'],age=person['age'])
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (email, name, phone_number, age) VALUES (?, ?, ?, ?)',
                       (user.email, user.name, user.phone_number, user.age))
        conn.commit()
        conn.close()
    return render_template("sing_up.html")

@app.route('/')
def sing_in():
    return render_template('sing_in.html')

@app.route('/',methods = ["POST"])
def sing_in1():
    if request.method == "POST":
        email = request.form['email']
        
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute('SELECT name,age FROM users WHERE email = ?', (email,))
        

        name = cursor.fetchone()


        cursor.close()
        conn.close()

        if name:
            return render_template('index.html')

    return render_template('sing_in.html')

if __name__ == '__main__':
    app.run(debug=True)