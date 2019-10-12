# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my API!"

if __name__ == "__main__":
    app.run(debug=True)

