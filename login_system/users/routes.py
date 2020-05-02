from login_system import db  # needed
from flask import Blueprint, render_template, redirect, url_for, request

users = Blueprint('users', __name__)


@users.route('/home/', methods=['GET', 'POST'])
def home():

    data = request.args.get('email')

    print(data)

    return render_template('user_templates/home.htm', title='Home Page', email=data)


@users.route('/register', methods=['GET', 'POST'])
def register():

    form_data = request.form
    from login_system.users.models import User

    username = form_data.get('username')
    email = form_data.get('email')
    gender = form_data.get('gender')
    password = form_data.get('password')

    if username or email or password or gender:
        user = User(username=username, email=email,
                    password=password, gender=gender)
        db.session.add(user)
        db.session.commit()
        print(f'user {user} created')
        return redirect('login')

    return render_template('user_templates/register.htm', title='Register')


@users.route('/login', methods=['GET', 'POST'])
def login():
    form_data = request.form
    from login_system.users.models import User

    email = form_data.get('email')
    password = form_data.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        return redirect('home')

    return render_template('user_templates/login.htm', title='Login')
