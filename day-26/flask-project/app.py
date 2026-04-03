from flask import Flask

app = Flask(__name__)#creteas web application

@app.route('/')#this create route
def home():
    return "Hello Students! Flask is running 🚀"

if __name__ == '__main__':
    app.run(debug=True)
