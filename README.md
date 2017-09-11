# Student Admin Panel

This flask application has used flask_admin package to do basic CRUD operations on basic student's records. In addition to these operations, we can easily use filtering, sorting kind of stuffs easily using flask_admin. Another great thing about his application is, this can handle importing of GBs of CSV data using panda which reads can read the file by chunk and we can write those to database :)

  - Uses SQLAlchemy, postgresql, flask_admin, pandas
  - jinja2 template and flask_admin uses bootstrap3

### How to run

I really love to create virtual environment for each and every projects and supply requirements.txt file for them. This way my system is always fresh and clean.

```sh
# Create a virtual environment for this app
$ virtualenv projectenv
# Activate the app's virtual environment
$ source projectenv/bin/activate
$ cd flask-admin-example
# Then install all dependencies using 
# requirements.txt file included with the project
$ pip install -r requirements.txt
# Run and get output csv file
$ python run.py
```

Please try this out and let me know.
### Thank You!!

