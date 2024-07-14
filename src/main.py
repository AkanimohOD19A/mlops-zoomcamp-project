# src/main.py
from src import app
from flask import request, render_template
from werkzeug.utils import secure_filename
import os
import src.model as model


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        filename = secure_filename(file.filename)
        file_path = os.path.join("uploads", filename)
        file.save(file_path)

        prediction = model.predict(file_path)

        return render_template("predict.html", image_file_name=filename, val=prediction)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
