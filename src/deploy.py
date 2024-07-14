# src/deploy.py
import os
import numpy as np
from PIL import Image
import tensorflow as tf
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, send_from_directory, jsonify

UPLOAD_FOLDER = '/Users/oelghareeb/Fashion_MNIST_MLOps/uploads'
app = Flask(__name__, template_folder='../templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model
model = tf.keras.models.load_model('s3://your-bucket/fashion_mnist_model_final.h5')


# Preprocess function
def preprocess_data(image):
    image = image.resize((28, 28)).convert('L')
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=-1)  # Add channel dimension
    return image


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            image = Image.open(filepath)
            processed_image = preprocess_data(image)
            prediction = model.predict(np.array([processed_image]))
            predicted_class = np.argmax(prediction)

            class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                           'Ankle boot']
            val = class_names[predicted_class]

            return render_template('predict.html', image_file_name=filename, val=val)
    return render_template("index.html")


@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
