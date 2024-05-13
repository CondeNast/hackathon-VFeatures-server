from app import app
from flask import render_template, request, jsonify
from summarizer import summarize_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']
        summarized_text = summarize_text(text)
        return jsonify({'summarized_text': summarized_text})
