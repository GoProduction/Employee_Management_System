from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


def customers():
    # this is a comment
    return null

if __name__ == "__main__":
    app.run()
