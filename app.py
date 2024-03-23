from flask import Flask,request,render_template,redirect,url_for
import mysql.connector

app = Flask(__name__)

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd",
        database="lab4"
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        name=request.form['name']
        address=request.form['address']
        email=request.form['email']
        mobile=request.form['mobile']
        cursor=conn.cursor()
        cursor.execute("INSERT INTO users (name, address, email, mobile) values(%s,%s,%s,%s)",(name, address, email, mobile))
        conn.commit()
        return redirect(url_for('home',message='Student Added Successfully!'))
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