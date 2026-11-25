from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "demo-only-secret"

@app.route("/")
def dashboard():
    return render_template("dashboard.html", active="dashboard")

@app.route("/import", methods=["GET", "POST"])
def import_resume():
    if request.method == "POST":
        filename = request.files.get("resume")
        if filename and filename.filename:
            flash("Demo mode: file upload received. OCR extraction is not connected yet.")
            return redirect(url_for("editor"))
        flash("Please choose a PDF or image file first.")
    return render_template("import.html", active="import")

@app.route("/editor")
def editor():
    return render_template("editor.html", active="editor")

@app.route("/assistant")
def assistant():
    return render_template("assistant.html", active="assistant")

@app.route("/templates")
def templates_page():
    return render_template("templates.html", active="templates")

@app.route("/preview")
def preview():
    return render_template("preview.html", active="preview")

@app.route("/resumes")
def resumes():
    return render_template("resumes.html", active="resumes")

if __name__ == "__main__":
    app.run(debug=True)
