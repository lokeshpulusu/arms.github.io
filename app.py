from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # Check if username and password are correct
    if username == "myuser" and password == "mypassword":
        return "Login successful!"
    else:
        return "Invalid username or password"

if __name__ == "__main__":
    app.run()
