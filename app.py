from flask import Flask, render_template,request
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    print(f"New message from {name} ({email}): {message}")
    return "Message Sent!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # fallback to 5000 locally
    app.run(host='0.0.0.0', port=port, debug=True)
