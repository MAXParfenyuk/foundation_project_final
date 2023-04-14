from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import BookForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_book.html", form=form)

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_book.html", form=form, book=book)

@app.route("/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)