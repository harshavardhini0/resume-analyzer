from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from resume_parser import extract_text, extract_skills
from job_matcher import match_jobs

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Backend is running"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['resume']

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    text = extract_text(path)

    if text == "error":
        return jsonify({"error": "File could not be read"}), 400

    if text == "unsupported":
        return jsonify({"error": "Unsupported file type"}), 400

    skills = extract_skills(text)
    jobs, suggestions = match_jobs(skills)

    return jsonify({
    "skills": skills,
    "jobs": jobs,
    "suggestions": suggestions
})

if __name__ == '__main__':
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=10000)