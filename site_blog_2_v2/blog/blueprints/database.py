from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin

db = SQLAlchemy()
migrate = Migrate()


def init_app(app) -> None:
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    name_user = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(102), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name: str, name_user: str, password: str) -> None:
        self.name = name
        self.name_user = name_user
        self.password = password


class Post(UserMixin, db.Model):
    __tablename__ = "posts"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(1500), nullable=False)
    created_date_time = db.Column(db.String(16), nullable=False)
    updated_date_time = db.Column(db.String(16), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(
        self,
        title: str,
        text: str,
        created_date_time: str,
        updated_date_time: str,
        users_id: int,
    ) -> None:
        self.title = title
        self.text = text
        self.created_date_time = created_date_time
        self.updated_date_time = updated_date_time
        self.users_id = users_id
