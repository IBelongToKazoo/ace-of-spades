import os
from flask import Flask, flash, request, redirect, url_for, render_template
import PyPDF2
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = r"C:\Users\Dell\OneDrive - ateneo.edu (1)\AY24-25 INTERSESH\ITMGT 25.03\ace-of-spades\uploads"
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#step 1 of quiz generator: upload PDF with reading
@app.route("/quiz", methods=['GET', 'POST'])
def quiz_generator():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
        
    return  render_template('quiz.html')

@app.route("/", methods=['GET']) #this could be the login page
def index():
    return 'Welcome to StraightAs!'
        
if __name__ == '__main__':
    app.run(debug=True)