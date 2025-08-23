from flask import Flask, render_template, request, flash


app: Flask = Flask(__name__)

@app.route("/")
def index() -> str:
    return render_template("index.html")

# Add a function to get the input from index.html


if __name__ == "__main__":
    app.run(debug=True)
