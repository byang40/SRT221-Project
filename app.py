from flask import Flask,request,render_template,redirect,url_for
import mysql.connector

app = Flask(__name__)

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd",
        database="project"
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = %s AND password = %s", (username, password,))
        user = cursor.fetchone()
        if user:
            # User exists and password matches
            return redirect(url_for('home'))  # Redirect to home or dashboard
        else:
            # User doesn't exist or password doesn't match
            return 'Invalid credentials', 401  # or you could redirect to login page again with an error message
    return render_template('login.html')  # Show the login form

@app.route('/add', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        name=request.form['name']
        address=request.form['address']
        email=request.form['email']
        mobile=request.form['mobile']
        cursor=conn.cursor()
        cursor.execute("INSERT INTO users (username, password, name, address, email, mobile) values(%s,%s,%s,%s,%s,%s)",(username, password, name, address, email, mobile))
        conn.commit()
        return redirect(url_for('home',message='User Created Successfully!'))
    return render_template('add_user.html')

@app.route('/view')
def view_users():
    cursor=conn.cursor()
    cursor.execute("select * from users")
    users=cursor.fetchall()
    return render_template('view_users.html',users=users)

@app.route('/delete/<int:id>',methods=['GET'])
def delete_user(id):
    cursor=conn.cursor()
    cursor.execute('DELETE from users where id=%s',(id,))
    conn.commit()
    return redirect(url_for('view_users'))

@app.route('/update/<int:id>', methods=['GET','POST'])
def update_user(id):
    cursor=conn.cursor()
    if request.method=='POST':
        name=request.form['name']
        address=request.form['address']
        email=request.form['email']
        mobile=request.form['mobile']
        cursor.execute('UPDATE users set name=%s, address=%s, email=%s, mobile=%s where id=%s',(name,address,email,mobile,id))
        conn.commit()
        return redirect(url_for('view_users'))
    cursor.execute('select * from users where id=%s',(id,))
    user=cursor.fetchone()
    return render_template('update_user.html',user=user)

if __name__=='__main__':
    app.run(debug=True)