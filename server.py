from flask import Flask, request, jsonify
from summarizer import Summarizer
from flask_cors import CORS
from PyPDF2 import PdfReader

app = Flask(__name__)
CORS(app)

bert_model = Summarizer()

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    pdf_reader = PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        print(page)
        text += page.extract_text()
    
    summarized_text = bert_summarize(text)
    return summarized_text

def bert_summarize(text):
    return ''.join(bert_model(text, min_length=60))

if __name__ == '__main__':
    app.run(debug=True)
