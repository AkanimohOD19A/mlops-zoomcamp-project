import os
import tempfile
import pytest  # type: ignore
from src.deploy import app  # Update this import to match the location of your deploy.py


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()  # Use a temporary directory for uploads

    with app.test_client() as client:
        yield client

    # Cleanup: remove temporary upload directory
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(file_path)
    os.rmdir(app.config['UPLOAD_FOLDER'])


def test_upload_form(client):
    """Test that the upload form is accessible"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Upload Image' in rv.data


def test_upload_file(client):
    """Test file upload"""
    data = {
        'image': (tempfile.NamedTemporaryFile(delete=False), 'test.png')  # Create a temporary file
    }
    rv = client.post('/', content_type='multipart/form-data', data=data, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Prediction' in rv.data  # Update this based on what you expect to see in the response


def test_upload_no_file(client):
    """Test uploading with no file"""
    rv = client.post('/upload', data={}, follow_redirects=True)
    assert rv.status_code == 405
    assert b'File type not allowed' not in rv.data
