from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Server pornit!"

if __name__ == '__main__':
    app.run()
add server.py cu cod flask simplu
