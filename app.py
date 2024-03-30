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
        cursor.close()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT idarticles, title, content, publication_date FROM articles ORDER BY publication_date DESC LIMIT 3")
    latest_articles = cursor.fetchall()
    cursor.close()
    return render_template('home.html', logged_in_user=logged_in_user, latest_articles=latest_articles)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password,))
        user = cursor.fetchone()
        cursor.close()
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

@app.route('/news')
def news():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles ORDER BY publication_date DESC")
    articles = cursor.fetchall()
    articles_list = []
    for article in articles:
        articles_list.append({
            'id': article[0],
            'title': article[1],
            'content': article[2],
            'publication_date': article[3]
        })
    cursor.close()
    logged_in_user = 'username' in session
    return render_template('news.html', articles=articles_list, logged_in_user=logged_in_user)

@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (title, content) VALUES (%s, %s)", (title, content))
        conn.commit()
        cursor.close()
        return redirect(url_for('news'))
    return render_template('add_article.html')

@app.route('/article/<int:article_id>', methods=['GET', 'POST'])
def article(article_id):
    if request.method == 'POST':
        # Check if the user is logged in
        if 'username' in session:
            comment = request.form['comment']
            author_name = session.get('username')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO comments (article_id, author_name, comment) VALUES (%s, %s, %s)", (article_id, author_name, comment))
            conn.commit()
            cursor.close()
        else:
            flash('You must be logged in to post a comment.', 'warning')
            return redirect(url_for('login'))
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM articles WHERE idarticles = %s", (article_id,))
    article = cursor.fetchone()
    cursor.execute("SELECT author_name, comment, comment_date FROM comments WHERE article_id = %s ORDER BY comment_date DESC", (article_id,))
    comments = cursor.fetchall()
    cursor.close()
    print(comments)  # Debug print to check the structure of comments
    return render_template('article_detail.html', article=article, comments=comments)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        flash('Please login to view your profile.', 'error')
        return redirect(url_for('login'))
    username = session['username']
    cursor = conn.cursor()
    cursor.execute("SELECT idusers, name, address, email, mobile FROM users WHERE username = %s", (username,))
    user_details = cursor.fetchone()
    cursor.execute("SELECT selectioncourse FROM courseselection WHERE user_id = %s", (user_details[0],))
    selected_courses = cursor.fetchall()
    total_cost = len(selected_courses) * 2000
    return render_template('profile.html', user_details=user_details, selected_courses=selected_courses, total_cost=total_cost)

@app.route('/courses')
def courses():
    cursor = conn.cursor()
    cursor.execute("SELECT coursename, coursedescription, coursecost FROM courses")
    courses = cursor.fetchall()
    return render_template('courses.html', courses=courses)

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if 'username' not in session:
        flash('Please login to enroll in courses', 'error')
        return redirect(url_for('login'))
    cursor = conn.cursor()
    if request.method == 'POST':
        username = session['username']
        cursor.execute("SELECT idusers FROM users WHERE username = %s", (username,))
        user_id_result = cursor.fetchone()
        if not user_id_result:
            flash('Error: User not found. Please try logging in again.', 'error')
            return redirect(url_for('login'))
        user_id = user_id_result[0]
        selected_courses = request.form.getlist('selected_courses')
        if not selected_courses:
            flash("Please select at least one course.", "error")
            return redirect(url_for('courses'))
        for course_name in selected_courses:
            cursor.execute("SELECT * FROM courseselection WHERE user_id = %s AND selectioncourse = %s", (user_id, course_name))
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO courseselection (selectioncourse, user_id) VALUES (%s, %s)", (course_name, user_id))
            else:
                flash(f"You are already enrolled in {course_name}.", "info")
        conn.commit()
        return redirect(url_for('confirmation'))
    else:
        cursor.execute("SELECT coursename FROM courses")
        courses = cursor.fetchall()
        return render_template('enroll.html', courses=courses)

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    if 'username' not in session:
        flash('Please login to view your course confirmation.', 'error')
        return redirect(url_for('login'))
    username = session['username']
    cursor = conn.cursor()
    cursor.execute("SELECT idusers FROM users WHERE username = %s", (username,))
    user_id_result = cursor.fetchone()
    if not user_id_result:
        flash('User not found. Please login again.', 'error')
        return redirect(url_for('login'))
    user_id = user_id_result[0]
    if request.method == 'POST':
        if 'delete' in request.form:
            course_to_delete = request.form['delete']
            cursor.execute("DELETE FROM courseselection WHERE selectioncourse = %s AND user_id = %s", (course_to_delete, user_id))
            conn.commit()
        elif 'add' in request.form:
            course_to_add = request.form['add']
            cursor.execute("INSERT INTO courseselection (selectioncourse, user_id) VALUES (%s, %s)", (course_to_add, user_id))
            conn.commit()
        return redirect(url_for('confirmation'))
    else:
        cursor.execute("SELECT selectioncourse FROM courseselection WHERE user_id = %s", (user_id,))
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