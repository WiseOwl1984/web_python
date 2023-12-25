from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Flask!</h1>"

@app.route("/page_2")
def p2():
    return "<h1>Hello from PAGE 2</h1>"
if __name__ == "__main__":
    app.run()