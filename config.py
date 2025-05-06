import os

class Config:
    SECRET_KEY = 'your-secret-key'  # Replace with a secure key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}