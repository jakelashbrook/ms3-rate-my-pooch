import os
from flask import Flask
if os.path.exists("env.py"): # allows the app to read the hidden env file
    import env


app = Flask(__name__) # creates an instance of the Flask app

@app.route("/")
def hello():
    return "Hello world.... AGAIN"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), # tells the app the host IP stored in env.py
            port=int(os.environ.get("PORT")), # fetches the port and turns it into a readable integer
            debug=True) # allows us to see actual errors that appear during development, make false before deployment.
