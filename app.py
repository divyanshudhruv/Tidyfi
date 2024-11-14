from flask import Flask, render_template, request, jsonify
import os
import shutil
from static.style import get_css

app = Flask(__name__)

# Define file categories and extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

# Organize files based on their type
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            continue

        file_moved = False
        for category, extensions in file_categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                category_folder = os.path.join(directory, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                file_moved = True
                break

        if not file_moved:
            others_folder = os.path.join(directory, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

@app.route('/style.css')
def style_css():
    return get_css()
# Route to render the HTML template
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        directory = request.form.get("directory")
        if os.path.isdir(directory):
            organize_files(directory)
            message = "Organized successfully!"
        else:
            message = "Invalid directory."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=False)
