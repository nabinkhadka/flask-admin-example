from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin
from app.students_admin_view import StudentsAdminView

app = Flask(__name__)
app_settings = 'app.config.DevelopmentConfig'
app.config.from_object(app_settings)
db = SQLAlchemy(app)

admin = flask_admin.Admin(
    app=app,
    url='/',
    name='Student Database',
    template_mode='bootstrap3'
)


from app import views, models

admin.add_view(StudentsAdminView(models.Student, db.session))
