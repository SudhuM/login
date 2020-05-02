from login_system import db, create_app

app = create_app()


def create_db():
    with app.app_context():
        db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    gender = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'username =  {self.username} , email  = {self.email}'
