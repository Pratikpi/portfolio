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
    filename = 'Pratik-Ingale_Senior-Software-Engineer.pdf'
    files_dir = os.path.join(current_app.root_path, 'static/files')
    if not os.path.isfile(os.path.join(files_dir, filename)):
        abort(404)
    return send_from_directory(
        files_dir,
        filename,
        as_attachment=True,
        download_name=filename,
    )
