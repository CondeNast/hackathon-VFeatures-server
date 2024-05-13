from flask import Flask, request, jsonify
from summarizer import Summarizer
from flask_cors import CORS
import PyPDF2

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

    if file and file.filename.endswith('.pdf'):
        pdf_text = extract_text_from_pdf(file)
        summarized_text = bert_summarize(pdf_text)
        return jsonify({'summary': summarized_text})
    else:
        return jsonify({'error': 'Unsupported file format'})

def extract_text_from_pdf(file):
    pdf_text = ''
    with open(file.filename, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            pdf_text += page.extractText()
    return pdf_text

def bert_summarize(text):
    return ''.join(bert_model(text, min_length=60))

if __name__ == '__main__':
    app.run(debug=True)
