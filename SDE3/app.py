# from flask import Flask, request, render_template, redirect, url_for, send_from_directory
# import os
# import shutil
# import boto3
# from botocore.exceptions import NoCredentialsError


# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/primary/'
# app.config['BACKUP_FOLDERS'] = ['uploads/backup1/', 'uploads/backup2/']
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

# # AWS S3 Configuration
# app.config['S3_BUCKET_NAME'] = 'userbucket1111'
# app.config['AWS_ACCESS_KEY'] = 'AKIA6ELKOMC2SDI5B65J'
# app.config['AWS_SECRET_KEY'] = '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'
# app.config['AWS_REGION'] = 'eu-north-1'

# # Initialize S3 client
# s3_client = boto3.client(
#     's3',
#     aws_access_key_id=app.config['AWS_ACCESS_KEY'],
#     aws_secret_access_key=app.config['AWS_SECRET_KEY'],
#     region_name=app.config['AWS_REGION']
# )

# # Ensure the local upload folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# for folder in app.config['BACKUP_FOLDERS']:
#     os.makedirs(folder, exist_ok=True)

# @app.route('/')
# def index():
#     files = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', files=files)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
        
#         # Save file to the primary local folder
#         primary_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(primary_path)

#         # Save copies to local backup folders
#         for folder in app.config['BACKUP_FOLDERS']:
#             shutil.copy(primary_path, folder)

#         # Upload to S3 bucket
#         try:
#             s3_client.upload_file(primary_path, app.config['S3_BUCKET_NAME'], file.filename)
#             print(f"File uploaded to S3: {file.filename}")
#         except NoCredentialsError:
#             return "AWS credentials not available", 403

#         return redirect(url_for('index'))
#     return render_template('upload.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route('/download/<filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# @app.route('/cdn/<filename>')
# def cdn_file(filename):
#     # Check local backups first
#     for folder in app.config['BACKUP_FOLDERS']:
#         backup_path = os.path.join(folder, filename)
#         if os.path.exists(backup_path):
#             return send_from_directory(folder, filename)
    
#     # Fall back to S3 if file not found in local backups
#     try:
#         url = s3_client.generate_presigned_url(
#             'get_object',
#             Params={'Bucket': app.config['S3_BUCKET_NAME'], 'Key': filename},
#             ExpiresIn=3600  # URL expiration time in seconds
#         )
#         return redirect(url)
#     except NoCredentialsError:
#         return "AWS credentials not available", 403
#     except Exception as e:
#         return f"File not found: {str(e)}", 404

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
# import os
# import shutil
# import boto3
# from botocore.exceptions import NoCredentialsError

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/primary/'
# app.config['BACKUP_FOLDERS'] = ['uploads/backup1/', 'uploads/backup2/']
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
# app.secret_key = 'your_secret_key'  # Required for flash messages

# # AWS S3 Configuration
# app.config['S3_BUCKET_NAME'] = 'userbucket1111'
# app.config['AWS_ACCESS_KEY'] = 'AKIA6ELKOMC2SDI5B65J'
# app.config['AWS_SECRET_KEY'] = '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'
# app.config['AWS_REGION'] = 'eu-north-1'

# # Initialize S3 client
# s3_client = boto3.client(
#     's3',
#     aws_access_key_id=app.config['AWS_ACCESS_KEY'],
#     aws_secret_access_key=app.config['AWS_SECRET_KEY'],
#     region_name=app.config['AWS_REGION']
# )

# # Ensure the local upload folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# for folder in app.config['BACKUP_FOLDERS']:
#     os.makedirs(folder, exist_ok=True)

# @app.route('/')
# def index():
#     files = os.listdir(app.config['UPLOAD_FOLDER'])
#     return render_template('index.html', files=files)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
        
#         # Save file to the primary local folder
#         primary_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(primary_path)

#         # Save copies to local backup folders
#         for folder in app.config['BACKUP_FOLDERS']:
#             shutil.copy(primary_path, folder)

#         # Upload to S3 bucket
#         try:
#             s3_client.upload_file(primary_path, app.config['S3_BUCKET_NAME'], file.filename)
#             flash(f"File uploaded to S3: {file.filename}")
#         except NoCredentialsError:
#             flash("AWS credentials not available", 'error')
#             return redirect(url_for('index'))

#         return redirect(url_for('index'))
#     return render_template('upload.html')

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route('/download/<filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# @app.route('/cdn/<filename>')
# def cdn_file(filename):
#     # Check local backups first
#     for folder in app.config['BACKUP_FOLDERS']:
#         backup_path = os.path.join(folder, filename)
#         if os.path.exists(backup_path):
#             return send_from_directory(folder, filename)
    
#     # Fall back to S3 if file not found in local backups
#     try:
#         url = s3_client.generate_presigned_url(
#             'get_object',
#             Params={'Bucket': app.config['S3_BUCKET_NAME'], 'Key': filename},
#             ExpiresIn=3600  # URL expiration time in seconds
#         )
#         return redirect(url)
#     except NoCredentialsError:
#         return "AWS credentials not available", 403
#     except Exception as e:
#         return f"File not found: {str(e)}", 404

# @app.route('/delete/<filename>', methods=['POST'])
# def delete_file(filename):
#     # Delete from primary and backup folders
#     try:
#         os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         for folder in app.config['BACKUP_FOLDERS']:
#             backup_path = os.path.join(folder, filename)
#             if os.path.exists(backup_path):
#                 os.remove(backup_path)
        
#         # Delete from S3
#         try:
#             s3_client.delete_object(Bucket=app.config['S3_BUCKET_NAME'], Key=filename)
#             flash(f"File '{filename}' deleted successfully.")
#         except NoCredentialsError:
#             flash("AWS credentials not available for deleting file from S3.", 'error')
#             return redirect(url_for('index'))
#         except Exception as e:
#             flash(f"Failed to delete file from S3: {str(e)}", 'error')

#     except FileNotFoundError:
#         flash(f"File '{filename}' not found locally.", 'error')
#     except Exception as e:
#         flash(f"Error deleting file '{filename}': {str(e)}", 'error')

#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)









from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import os
import shutil
import boto3
from botocore.exceptions import NoCredentialsError

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/primary/'
app.config['BACKUP_FOLDERS'] = ['uploads/backup1/', 'uploads/backup2/']
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for flash messages and session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect unauthorized users to login

# AWS S3 Configuration
app.config['S3_BUCKET_NAME'] = 'userbucket1111'
app.config['AWS_ACCESS_KEY'] = 'AKIA6ELKOMC2SDI5B65J'
app.config['AWS_SECRET_KEY'] = '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'
app.config['AWS_REGION'] = 'eu-north-1'

# Initialize S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=app.config['AWS_ACCESS_KEY'],
    aws_secret_access_key=app.config['AWS_SECRET_KEY'],
    region_name=app.config['AWS_REGION']
)

# Ensure the local upload folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
for folder in app.config['BACKUP_FOLDERS']:
    os.makedirs(folder, exist_ok=True)

# User model for authentication
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route to register new users
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists
        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "danger")
            return redirect(url_for('register'))
        
        # Hash the password and create a new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password.", "danger")
    return render_template('login.html')

# Route for logging out users
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# Home page showing file list (Login required)
@app.route('/')
@login_required
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

# Route for file upload (Login required)
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file selected.", "danger")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("No file selected.", "danger")
            return redirect(request.url)
        
        primary_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(primary_path)

        for folder in app.config['BACKUP_FOLDERS']:
            shutil.copy(primary_path, folder)

        try:
            s3_client.upload_file(primary_path, app.config['S3_BUCKET_NAME'], file.filename)
            flash(f"File uploaded to S3: {file.filename}")
        except NoCredentialsError:
            flash("AWS credentials not available", 'error')
            return redirect(url_for('index'))

        return redirect(url_for('index'))
    return render_template('upload.html')

# Route for file download (Login required)
@app.route('/download/<filename>')
@login_required
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# Route for CDN access (backup and S3 access) (Login required)
@app.route('/cdn/<filename>')
@login_required
def cdn_file(filename):
    for folder in app.config['BACKUP_FOLDERS']:
        backup_path = os.path.join(folder, filename)
        if os.path.exists(backup_path):
            return send_from_directory(folder, filename)
    
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': app.config['S3_BUCKET_NAME'], 'Key': filename},
            ExpiresIn=3600
        )
        return redirect(url)
    except NoCredentialsError:
        return "AWS credentials not available", 403
    except Exception as e:
        return f"File not found: {str(e)}", 404

# Route to delete a file (Login required)
@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    try:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        for folder in app.config['BACKUP_FOLDERS']:
            backup_path = os.path.join(folder, filename)
            if os.path.exists(backup_path):
                os.remove(backup_path)
        
        try:
            s3_client.delete_object(Bucket=app.config['S3_BUCKET_NAME'], Key=filename)
            flash(f"File '{filename}' deleted successfully.")
        except NoCredentialsError:
            flash("AWS credentials not available for deleting file from S3.", 'error')
        except Exception as e:
            flash(f"Failed to delete file from S3: {str(e)}", 'error')

    except FileNotFoundError:
        flash(f"File '{filename}' not found locally.", 'error')
    except Exception as e:
        flash(f"Error deleting file '{filename}': {str(e)}", 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(host="0.0.0.0", port=5000)

