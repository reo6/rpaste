from flask import Flask, \
                  render_template, \
                  request, \
                  redirect
from .settings import DB_FILE
from tinydb import TinyDB
from .paste import Paste

app = Flask(__name__, static_folder="static")
db = TinyDB(DB_FILE)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    print("Saving new..")
    paste = Paste.create(
        db,
        request.form["content"],
        request.form["description"]
    )
    paste.save(db)
    return redirect(f"/p/{paste.id}")

@app.route("/p/<id>")
def get_paste(id):
    paste = Paste.get(db, id)
    return render_template("paste.html", paste=paste)
