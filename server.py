from flask import Flask, request, send_from_directory, render_template_string
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def hello():
    return 'Server pornit!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No image part in request', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return f'Poza {file.filename} a fost salvata cu succes!', 200

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/galerie')
def galerie():
    poze = os.listdir(UPLOAD_FOLDER)
    html = """
    <h1>Galerie Foto</h1>
    {% for poza in poze %}
        <div style="margin-bottom: 20px;">
            <img src="/uploads/{{ poza }}" alt="{{ poza }}" style="max-width: 100%; height: auto;" />
            <p>{{ poza }}</p>
        </div>
    {% endfor %}
    """
    return render_template_string(html, poze=poze)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
