from flask import Flask, render_template,request
app = Flask(__name__)


@app.route("/")
def default_page():
    return "<html><body>Hello World</body></html>"


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)