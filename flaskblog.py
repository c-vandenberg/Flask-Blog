from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# Configure app with secret key which is used to sign session cookies. This protects user session cookies from cookie data tampering, forgery attacks etc
app.config['SECRET_KEY'] = '9b974a41c755a417ba62adf0bce74009'

posts = [
    {
        'author': 'Chris van den Berg',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 16th. 2018'
    },
    {
        'author': 'Grace Hurdle',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 16th. 2018'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Create instance of RegistrationForm Class
    form = RegistrationForm()
    # Check if form validates correctly when submitted
    if form.validate_on_submit():
        flash(f'Account Created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Create instance of LoginForm Class
    form = LoginForm()
    # Check if form validates correctly when submitted
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)