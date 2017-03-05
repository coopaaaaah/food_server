from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/<id>")
def getId(id):
    return "This is your id: " + id

if __name__ == "__main__":
    app.run()
