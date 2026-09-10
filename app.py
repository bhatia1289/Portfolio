from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/my_resume')
def my_resume():
    return render_template('resume.html')

@app.route('/my_projects')
def my_projects():
    return render_template('projects.html')

@app.route('/contact')
def contact_me():
    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

if __name__ == '__main__':
    app.run(debug = True)
