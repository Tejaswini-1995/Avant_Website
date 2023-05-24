from flask import Flask, render_template
# from flask_ngrok import run_with_ngrok 

app = Flask(__name__)
# run_with_ngrok(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
    
    
if __name__ == '__main__':
    app.run()
    # serve(app, host='127.0.0.1', port=8080, url_scheme='https')

    