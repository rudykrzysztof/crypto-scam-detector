from flask import Flask, render_template, request
from detector.analyzer import analyze_project_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form.get("project_text", "")
        result = analyze_project_text(text)

    return render_template("index.html", result=result, text=text)

if __name__ == "__main__":
    app.run(debug=True)
