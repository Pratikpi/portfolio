from flask import Blueprint, render_template, send_from_directory, current_app, abort
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/resume')
def download_resume():
    if not current_app.config['ENABLE_RESUME_DOWNLOAD']:
        abort(404)
    # Ensure the file exists in the right place, for now pointing to static/files
    # In a real scenario we'd rename the uploaded PDF to a standard name or config map it
    filename = 'Pratik-Ingale_Senior-Software-Engineer_Nokia.pdf' 
    # Try to serve from root or static/files. 
    # For this refactor, let's assume we'll move the file to app/static/files
    return send_from_directory(os.path.join(current_app.root_path, 'static/files'), filename)
