from flask import Flask, send_from_directory, render_template
# App and API setup
app = Flask(__name__, static_folder="static/static", template_folder="static")

# Serve React App
@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")