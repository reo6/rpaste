from flask import Flask, \
                  render_template, \
                  request, \
                  redirect
from .settings import DB_FILE, HCAPTCHA
from tinydb import TinyDB
from .paste import Paste
from flask_hcaptcha import hCaptcha
import os

app = Flask(__name__, static_folder="static")
app.config["HCAPTCHA_SITE_KEY"] = os.environ["HCAPTCHA_SITE_KEY"]
app.config["HCAPTCHA_SECRET_KEY"] = os.environ["HCAPTCHA_SECRET_KEY"]
hcaptcha = hCaptcha(app)

db = TinyDB(DB_FILE)

@app.route("/")
def home():
    return render_template("index.html", ishcaptcha=HCAPTCHA)

@app.route("/save", methods=["POST"])
def save():
    verify = hcaptcha.verify() if HCAPTCHA else True
    if verify:
        paste = Paste.create(
            db,
            request.form["content"],
            request.form["description"]
        )
        paste.save(db)
        return redirect(f"/p/{paste.id}")
    else:
        return redirect("/")

@app.route("/p/<id>")
def get_paste(id):
    paste = Paste.get(db, id)
    return render_template("paste.html", paste=paste)
