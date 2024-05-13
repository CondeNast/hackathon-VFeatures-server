# app/routes.py
from flask import Blueprint, request

# Create a blueprint
routes_blueprint = Blueprint('routes', __name__)

# Define route(s) within the blueprint
@routes_blueprint.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Handle file processing here
    # For example, save the file to a directory
    file.save('uploads/' + file.filename)

    return 'File uploaded successfully'
