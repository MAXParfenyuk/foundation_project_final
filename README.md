# Project Name

## Description
This is a Flask web application for managing books. It allows users to add, edit, and delete books using a web form. The application uses SQLAlchemy for database management and Flask-WTF for form handling.

## Features
- Add new books with title and author information
- Edit existing books
- Delete books
- Display a list of all books in the database

## Technologies Used
- Python
- Flask
- SQLAlchemy
- Flask-WTF

## Installation
1. Clone the repository to your local machine.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Create a SQLite database by running `python app.py db init`.
4. Migrate the database by running `python app.py db migrate` and `python app.py db upgrade`.
5. Start the application by running `python app.py`.

