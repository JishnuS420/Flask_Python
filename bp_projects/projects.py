from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@app_projects.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@app_projects.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'] )
def main():
    color = "FFFFFF"
    new_color = request.form.get('color', '')
    if re.search(r'^[0-9A-F]{6}$', new_color):
        color = new_color

    return render_template('main.html', color = color)