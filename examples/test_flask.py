from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello from Flask!<h1>"

@app.route("/second_page")
def page_2():
    return "<h1>Hello from Page 2!</h1>"

if __name__== "__main__":
    app.run()
