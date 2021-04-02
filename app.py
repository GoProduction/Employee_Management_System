from flask import Flask, render_template
import connection
import cx_Oracle
from controllers import employees_controller

app = Flask(__name__)

@app.route("/")
def index():
    employees_controller.get_employees
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    # this is a comment
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run()

