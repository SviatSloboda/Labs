from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route("/")
def index():
    return "<span style = 'color: red'>Wrong page</span>"


@app.route("/api/v1/hello-world-21")
def HelloWorld():
    return "<span style = 'color:blue; text-align:center;'>" \
           "<h1>Hello World 21</h1>" \
           "</span>"


if __name__ == '__main__':
    serve(app)

# http://localhost:8080/api/v1/hello-world-21

# waitress-serve --port=8080 --url-scheme=http main:app