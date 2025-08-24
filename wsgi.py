#!/usr/bin/python3.10

"""
WSGI configuration for PythonAnywhere deployment

Instructions for PythonAnywhere setup:

1. Upload your files to: /home/yourusername/mysite/
2. Replace 'yourusername' in this file with your actual PythonAnywhere username
3. Set environment variables in your .bashrc file
4. Make sure all requirements are installed: pip3.10 install --user -r requirements-pythonanywhere.txt
5. In the Web tab, set this file as your WSGI configuration file

Directory structure on PythonAnywhere should be:
/home/yourusername/mysite/
    ├── app_pythonanywhere.py
    ├── config_pythonanywhere.py
    ├── requirements-pythonanywhere.txt
    ├── static/
    └── templates/
"""

import sys
import os

# Add your project directory to the sys.path
# Replace 'yourusername' with your actual PythonAnywhere username
project_home = '/home/yourusername/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables (if not set in .bashrc)
os.environ.setdefault('FLASK_CONFIG', 'production')

# Import your Flask application
from app_pythonanywhere import app as application

# This is what PythonAnywhere will use as the WSGI application
if __name__ == "__main__":
    application.run()
