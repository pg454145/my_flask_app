from flask import Flas

app = Flask(__name__

@app.route("/")
def home():
    return "Hello, GitHub Deployment!"

if __name__ == "__main__":
    app.run(debug=True)
