from app import app
from app import csv_handler
from flask import request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'csv', 'CSV'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        _file = request.files['file']
        if _file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if _file and allowed_file(_file.filename):
            filename = secure_filename(_file.filename)
            _file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            handler = csv_handler.CSVHandler(filename)
            handler.start_job()
            flash('File uploaded successfully')
            return redirect('/')
        else:
            flash('Invalid file')
    return redirect('/')
