from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

"""
App.route is used to add pages. "/" mean main page we can also add a 
particular page name here

Also we create static folder and add some files in it and those files are downloadable
through link (original path/static/filename)

Templates Are used to store templates and render that templates.
"""
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TODO.db"

db = SQLAlchemy(app)

class TODO(db.Model):
    sno = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(100) , nullable = False)
    desc = db.Column(db.String(500) , nullable = False)
    date = db.Column(db.DateTime , default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/" , methods = ["get" , "post"])
def hello_world():
    if(request.method == "POST"):
        title = request.form["title"]
        desc = request.form["desc"]
        todo = TODO(title = title , desc = desc)
        db.session.add(todo)
        db.session.commit()
    all_todo = TODO.query.all()
    return render_template("index.html" , all_todo = all_todo)


@app.route("/show")
def show():
    all_todo = TODO.query.all()
    print(all_todo)
    return "Data Displayed"

@app.route("/update/<int:sno>" , methods = ["get" , "post"])
def update(sno):
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = TODO.query.filter_by(sno = sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = TODO.query.filter_by(sno = sno).first()
    return render_template("update.html" , todo = todo)


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = TODO.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/Page2")
def Page2():
    return("I am Page Number 2")

if __name__ == "__main__":
    app.run(debug = True , port = 8000)