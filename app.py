from flask import Flask,request,render_template,redirect,url_for,flash,session
import mysql.connector

app = Flask(__name__)

# Used for user session
app.secret_key = '4909cb823c299062746b3ff420b81f2e'

# MySQL database credentials needed to connect to it.
conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ssw0rd",
        database="project"
    )

# Defines a route for home page
@app.route('/')
def home():
    # Variable to store the current user logged in.
    logged_in_user = None
    print("Session Data:", session)
    # Checks the POST request to see if the inputs from the form matches the database
    if 'username' in session:
        username = session['username']
        # Used to connect to the database
        cursor = conn.cursor()
        # Executes the SQL query to select the user based on username
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        print("User Data:", user)
        # Used to close the cursor.
        cursor.close()
        if user:
            # Saves the 2nd element of the user from the users database.
            logged_in_user = {'username': user[1]}
        cursor.close()
    cursor = conn.cursor(dictionary=True)
    # # Executes the SQL query to retrieve the 3 recent articles based on their publication date from the database
    cursor.execute("SELECT idarticles, title, content, publication_date FROM articles ORDER BY publication_date DESC LIMIT 3")
    # Fetches the latest 3 articles from the database,
    latest_articles = cursor.fetchall()
    # Used to close the cursor.
    cursor.close()
    return render_template('home.html', logged_in_user=logged_in_user, latest_articles=latest_articles)

# Defines a route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Checks the POST request to see if the inputs from the form matches the database
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Used to connect to the database
        cursor = conn.cursor()
        # Executes the SQL query to retrieve the user based on username and password from the database.
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password,))
        user = cursor.fetchone()
        # Used to close the cursor.
        cursor.close()
        if user:
            # Store the user's username to the session
            session['username'] = username
            # Flashes a message if user has successfuly match the database
            flash('You were successfully logged in.', 'success')
            # Redirects user to home page
            return redirect(url_for('home'))
        else:
            # Flashes a message if username or password does not match the database
            flash('Invalid username or password', 'error')
            # Redirects user to login page
            return redirect(url_for('login')) 
    return render_template('login.html') 

# Defines a route for logout
@app.route('/logout')
def logout():
    # Removes user from the session
    session.pop('username', None)
    # Flashes a message that the user has logged out successfully
    flash('You were successfully logged out.', 'success')
    # Redirects the user back to home page
    return redirect(url_for('home'))

# Defines a route for forgot login page
@app.route('/forgotlogin', methods=['GET', 'POST'])
def forgot_login():
    # Checks the POST request to see if the inputs from the form matches the database
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Used to connect to the database
        cursor = conn.cursor()
        # Executes the SQL query to retrieve the user based on name and email from the database.
        cursor.execute("SELECT * FROM users WHERE name = %s AND email = %s", (name, email))
        user = cursor.fetchone()
        if user:
            # If the name and email matches the database then it will displayy all the information of that user from the database.
            return render_template('user_info.html', user=user)
        else:
            # If name and/or email does not match then it will prompt an error message.
            flash ('No user found with the provided name and email', 'error')
            # Redirects the user back to the forgot login page
            return redirect(url_for('forgot_login', message='User Does Not Exist'))
    return render_template('forgot_login_form.html')

# Defines a route for creating a user
@app.route('/add', methods=['GET','POST'])
def add_user():
    # Checks the POST request to see the inputs, retrieves them and inserts them into the database.
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        name=request.form['name']
        address=request.form['address']
        email=request.form['email']
        mobile=request.form['mobile']
        # Used to connect to the database
        cursor=conn.cursor()
        # Executes the SQL query to insert the information into the database
        cursor.execute("INSERT INTO users (username, password, name, address, email, mobile) values(%s,%s,%s,%s,%s,%s)",(username, password, name, address, email, mobile))
        # Used to commit the changes in the database.
        conn.commit()
        # Redirects user to home page
        return redirect(url_for('home'))
    return render_template('add_user.html')

# Defines a route for news page
@app.route('/news')
def news():
    # Used to connect to the database
    cursor = conn.cursor()
    # Executes the SQL query to retrieve all the articles from the table
    cursor.execute("SELECT * FROM articles ORDER BY publication_date DESC")
    articles = cursor.fetchall()
    articles_list = []
    # Loops article in articles that is being fetched from the database.
    for article in articles:
        # Appends the dictionary to articles_list with mathcing keys that will have the information extracted for display.
        articles_list.append({
            'id': article[0],
            'title': article[1],
            'content': article[2],
            'publication_date': article[3]
        })
    # Used to close the cursor.
    cursor.close()
    # Checks if username exist in the session to allow it to post an article
    logged_in_user = 'username' in session
    return render_template('news.html', articles=articles_list, logged_in_user=logged_in_user)

# Defines a route for add article page
@app.route('/add_article', methods=['GET', 'POST'])
def add_article():
    # Checks the POST request to see the inputs, retrieves them and inserts them into the database.
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # Used to connect to the database
        cursor = conn.cursor()
        # Executes the SQL query to insert title and content information into the database.
        cursor.execute("INSERT INTO articles (title, content) VALUES (%s, %s)", (title, content))
        # Used to commit the changes in the database.
        conn.commit()
        # Used to close the cursor.
        cursor.close()
        # Redirects user to news page.
        return redirect(url_for('news'))
    return render_template('add_article.html')

# Defines a route for article page
@app.route('/article/<int:article_id>', methods=['GET', 'POST'])
def article(article_id):
    if request.method == 'POST':
        # Check if the user is logged in
        if 'username' in session:
            comment = request.form['comment']
            author_name = session.get('username')
            # Used to connect to the database
            cursor = conn.cursor()
            # Executes the SQL query to insert new comment information into the database.
            cursor.execute("INSERT INTO comments (article_id, author_name, comment) VALUES (%s, %s, %s)", (article_id, author_name, comment))
            # Used to commit the changes in the database.
            conn.commit()
            # Used to close the cursor.
            cursor.close()
        else:
            # Flashes a message that prompts the user that they need to login inorder to make a comment.
            flash('You must be logged in to post a comment.', 'warning')
            # Redirects user to login page
            return redirect(url_for('login'))
    # Used to connect to the database to fetch data as a dictionary
    cursor = conn.cursor(dictionary=True)
    # Executes the SQL query to retrieve article_id information from database.
    cursor.execute("SELECT * FROM articles WHERE idarticles = %s", (article_id,))
    # Fetches the matching article
    article = cursor.fetchone()
    # Executes the SQL query to retrieve comments for the article based on when there date.
    cursor.execute("SELECT author_name, comment, comment_date FROM comments WHERE article_id = %s ORDER BY comment_date DESC", (article_id,))
    # Fetches all the matching comments.
    comments = cursor.fetchall()
    # Used to close the cursor.
    cursor.close()
    return render_template('article_detail.html', article=article, comments=comments)

# Defines a route for contacts page
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Defines a route for profile page
@app.route('/profile')
def profile():
    # Checks to see if user is logged in for the session.
    if 'username' not in session:
        # Flashes a message that user needs to be logged in to view the profile page.
        flash('Please login to view your profile.', 'error')
        # Redirects user to login page.
        return redirect(url_for('login'))
    # Retrieves the username from the session.
    username = session['username']
    # Used to connect to the database.
    cursor = conn.cursor()
    # Executes the SQL query to retrieve user details from the database.
    cursor.execute("SELECT idusers, name, address, email, mobile FROM users WHERE username = %s", (username,))
    # Fetches user details.
    user_details = cursor.fetchone()
    # Executes the SQL query to retrieve courses selected by the user.
    cursor.execute("SELECT selectioncourse FROM courseselection WHERE user_id = %s", (user_details[0],))
    # Festches all the selected courses.
    selected_courses = cursor.fetchall()
    # Shortcut to calculate all selected courses times 2000 to generate the price.
    total_cost = len(selected_courses) * 2000
    return render_template('profile.html', user_details=user_details, selected_courses=selected_courses, total_cost=total_cost)

# Defines a route for courses page
@app.route('/courses')
def courses():
    # Used to connect to the database.
    cursor = conn.cursor()
    # Executes the SQL query to retrieve all the courses from the database.
    cursor.execute("SELECT coursename, coursedescription, coursecost FROM courses")
    # Fetches all the courses.
    courses = cursor.fetchall()
    return render_template('courses.html', courses=courses)

# Defines a route for enroll page
@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    # Checks to see if user is logged into a session by checking 'username'.
    if 'username' not in session:
        # Flashes a message to users that they need to login to enroll into courses.
        flash('Please login to enroll in courses', 'error')
        # Redirects user to login page.
        return redirect(url_for('login'))
    # Used to connect to the database.
    cursor = conn.cursor()
    # Checks the POST request form submission.
    if request.method == 'POST':
        # Retrieves the current user logged into the session.
        username = session['username']
        # Executes the SQL query to retrieve user iduser that matches username from database.
        cursor.execute("SELECT idusers FROM users WHERE username = %s", (username,))
        user_id_result = cursor.fetchone()
        # Checks to see if the user is on the database.
        if not user_id_result:
            # Flashes a message that the user is not found and that you should relog.
            flash('Error: User not found. Please try logging in again.', 'error')
            # Redirects user to login page
            return redirect(url_for('login'))
        # If user is found, it will save the iduser into the variable.
        user_id = user_id_result[0]
        # Retrieves the selected courses from the form submission.
        selected_courses = request.form.getlist('selected_courses')
        # Checks to see if no course is selected.
        if not selected_courses:
            # Flashes a message to user that 1 course must be selected.
            flash("Please select at least one course.", "error")
            # Redirects user to course selection page.
            return redirect(url_for('courses'))
        # For loop to check if the course has already been selected by user so that cannot select it twice.
        for course_name in selected_courses:
            # Executes the SQL query to retrieve the selected course that matches the users id.
            cursor.execute("SELECT * FROM courseselection WHERE user_id = %s AND selectioncourse = %s", (user_id, course_name))
            if cursor.fetchone() is None:
                # # Executes the SQL query to insert the selected course into the database if not already enrolled.
                cursor.execute("INSERT INTO courseselection (selectioncourse, user_id) VALUES (%s, %s)", (course_name, user_id))
            else:
                # Flashes a message if the user has already enrolled into the course.
                flash(f"You are already enrolled in {course_name}.", "info")
        # Used to commit the changes in the database.
        conn.commit()
        # Redirects user to confirmation page
        return redirect(url_for('confirmation'))
    else:
        # Executes the SQL query to retrieve list of courses for display
        cursor.execute("SELECT coursename FROM courses")
        courses = cursor.fetchall()
        return render_template('enroll.html', courses=courses)

# Defines a route for confirmation page
@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    # Checks to see if user is logged into a session by checking 'username'.
    if 'username' not in session:
        # Flashes a message to users that they need to login to enroll into courses.
        flash('Please login to view your course confirmation.', 'error')
        # Redirects user to login page.
        return redirect(url_for('login'))
    # Retrieves the current user logged into the session.
    username = session['username']
    # Used to connect to the database
    cursor = conn.cursor()
    # Executes the SQL query to retrieve user iduser that matches username from database.
    cursor.execute("SELECT idusers FROM users WHERE username = %s", (username,))
    user_id_result = cursor.fetchone()
    # Checks if the user exists in the database.
    if not user_id_result:
        # Flashes a message to the user that the user is not found.
        flash('User not found. Please login again.', 'error')
        # Redirects to login page.
        return redirect(url_for('login'))
    # If user is found, it will save the iduser into the variable.
    user_id = user_id_result[0]
    # Checks the POST request form submission.
    if request.method == 'POST':
        # Checks if the user has requested to delete a course.
        if 'delete' in request.form:
            # Retrieves the course name that will be deleted from the form submission.
            course_to_delete = request.form['delete']
            # Executes the SQL query to delete the specified course.
            cursor.execute("DELETE FROM courseselection WHERE selectioncourse = %s AND user_id = %s", (course_to_delete, user_id))
            # Used to commit the changes in the database.
            conn.commit()
        # Checks if the user has requested to add a course.
        elif 'add' in request.form:
            # Retrieves the course name that will be added from the form submission.
            course_to_add = request.form['add']
            # Executes the SQL query to add the specified course.
            cursor.execute("INSERT INTO courseselection (selectioncourse, user_id) VALUES (%s, %s)", (course_to_add, user_id))
            # Used to commit the changes in the database.
            conn.commit()
        # Redirects user to the confirmation page.
        return redirect(url_for('confirmation'))
    else:
        # Executes the SQL query to retrieve all the courses the user has enrolled in.
        cursor.execute("SELECT selectioncourse FROM courseselection WHERE user_id = %s", (user_id,))
        # Fetches all the enrolled courses by the user.
        selected_courses = cursor.fetchall()
        # To calculate total cost later.
        total_cost = 0
        for course_name in selected_courses:
            # Executes the SQL query to retrieve cost of each course from database.
            cursor.execute("SELECT coursecost FROM courses WHERE coursename = %s", (course_name[0],))
            # Fetches the cost of the course.
            cost = cursor.fetchone()
            if cost:
                # Add the cost of each course to calculate the total.
                total_cost += cost[0]
        return render_template('confirmation.html', selected_courses=selected_courses, total_cost=total_cost)

if __name__=='__main__':
    app.run(debug=True)