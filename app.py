from flask import Flask,request,render_template,redirect,url_for,flash,session
import mysql.connector

app = Flask(__name__)
app.secret_key = '4909cb823c299062746b3ff420b81f2e'

conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd",
        database="project"
    )

@app.route('/')
def home():
    logged_in_user = None
    print("Session Data:", session)
    if 'username' in session:
        username = session['username']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        print("User Data:", user)
        cursor.close()
        if user:
            logged_in_user = {'username': user[1]}
    return render_template('home.html', logged_in_user=logged_in_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password,))
        user = cursor.fetchone()
        cursor.close()
        # conn.close()
        if user:
            session['username'] = username
            flash('You were successfully logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login')) 
    return render_template('login.html') 

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were successfully logged out.', 'success')
    return redirect(url_for('home'))

@app.route('/forgotlogin', methods=['GET', 'POST'])
def forgot_login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = %s AND email = %s", (name, email))
        user = cursor.fetchone()
        if user:
            return render_template('user_info.html', user=user)
        else:
            flash ('No user found with the provided name and email', 'error')
            return redirect(url_for('forgot_login', message='User Does Not Exist'))
    return render_template('forgot_login_form.html')

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

# @app.route('/view')
# def view_users():
#     cursor=conn.cursor()
#     cursor.execute("select * from users")
#     users=cursor.fetchall()
#     return render_template('view_users.html',users=users)

# @app.route('/delete/<int:id>',methods=['GET'])
# def delete_user(id):
#     cursor=conn.cursor()
#     cursor.execute('DELETE from users where id=%s',(id,))
#     conn.commit()
#     return redirect(url_for('view_users'))

# @app.route('/update/<int:id>', methods=['GET','POST'])
# def update_user(id):
#     cursor=conn.cursor()
#     if request.method=='POST':
#         name=request.form['name']
#         address=request.form['address']
#         email=request.form['email']
#         mobile=request.form['mobile']
#         cursor.execute('UPDATE users set name=%s, address=%s, email=%s, mobile=%s where id=%s',(name,address,email,mobile,id))
#         conn.commit()
#         return redirect(url_for('view_users'))
#     cursor.execute('select * from users where id=%s',(id,))
#     user=cursor.fetchone()
#     return render_template('update_user.html',user=user)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    cursor = conn.cursor()
    if request.method == 'POST':
        selected_courses = request.form.getlist('selected_courses')
        if not selected_courses:
            return render_template('enroll.html', courses=courses, error="Please select at least one course.")
        for course_name in selected_courses:
            cursor.execute("SELECT * FROM courseselection WHERE selectioncourse = %s", (course_name,))
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO courseselection (selectioncourse) VALUES (%s)", (course_name,))
        conn.commit()
        return redirect(url_for('confirmation'))
    else:
        cursor.execute("SELECT coursename FROM courses")
        courses = cursor.fetchall()
        return render_template('enroll.html', courses=courses)

@app.route('/courses')
def courses():
    cursor = conn.cursor()
    cursor.execute("SELECT coursename, coursedescription, coursecost FROM courses")
    courses = cursor.fetchall()
    return render_template('courses.html', courses=courses)

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    cursor = conn.cursor()
    if request.method == 'POST':
        if 'delete' in request.form:
            course_to_delete = request.form['delete']
            cursor.execute("DELETE FROM courseselection WHERE selectioncourse = %s", (course_to_delete,))
            conn.commit()
        elif 'add' in request.form:
            course_to_add = request.form['add']
            cursor.execute("INSERT INTO courseselection (selectioncourse) VALUES (%s)", (course_to_add,))
            conn.commit()
        return redirect(url_for('confirmation'))
    else:
        cursor.execute("SELECT selectioncourse FROM courseselection")
        selected_courses = cursor.fetchall()
        total_cost = 0
        for course_name in selected_courses:
            cursor.execute("SELECT coursecost FROM courses WHERE coursename = %s", (course_name[0],))
            cost = cursor.fetchone()
            if cost:
                total_cost += cost[0]
        return render_template('confirmation.html', selected_courses=selected_courses, total_cost=total_cost)

if __name__=='__main__':
    app.run(debug=True)