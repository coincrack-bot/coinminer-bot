from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # This will load templates/home.html

if __name__ == '__main__':
    app.run(debug=False, port=10000)
