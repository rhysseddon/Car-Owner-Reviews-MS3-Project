import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    """
    This function finds the reviews on mongo db adds to a list
    and display them in accordion on homepage.
    """
    reviews = list(mongo.db.reviews.find())
    return render_template("home.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    This function does a text search for make and model in the
    db. If admin searches on manage reviews page the results will
    display on manage reviews page, if not they display on home page.    
    """
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    if session["user"] == "admin":  # And on manage reviews page??
        return render_template("manage_reviews.html", reviews=reviews)

    return render_template("home.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This function checks for existing user in the db,
    saves username and password and put the new user into
    session cookie.
    """
    if request.method == "POST":
        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already taken!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome to the club!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This function checks username and password are correct
    and logs in user.
    """
    if request.method == "POST":
        # check for username in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    This function gets session user and their reviews from db
    and renders to the users profile page
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    reviews = list(mongo.db.reviews.find())
    if session["user"]:
        return render_template(
            "profile.html", username=username, reviews=reviews)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    This function upon a saving a review creates a
    dictionary and saves to db.
    """
    if request.method == "POST":
        review = {
            "make": request.form.get("make"),
            "model": request.form.get("model"),
            "year": request.form.get("year"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "owner": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_reviews"))

    makes = mongo.db.makes.find().sort("make", 1)
    return render_template("add_review.html", makes=makes)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    When an edited review is saved this function adds
    the edited data to the db and redirects to profile
    page, if its an admin edit on manage reviews page
    the owner will not be edited and will redirect to
    manage reviews page.
    """
    if request.method == "POST":
        if session["user"] == "admin":
            edited = {
                "make": request.form.get("make"),
                "model": request.form.get("model"),
                "year": request.form.get("year"),
                "review": request.form.get("review"),
                "rating": request.form.get("rating"),
                "owner": request.form.get("owner")
            }
        else:
            edited = {
                "make": request.form.get("make"),
                "model": request.form.get("model"),
                "year": request.form.get("year"),
                "review": request.form.get("review"),
                "rating": request.form.get("rating"),
                "owner": session["user"]
            }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, edited)
        flash("Review Successfully Edited")
        if session["user"] == "admin":
            return redirect(url_for(
                "get_manage", username=session["user"]))
        else:
            return redirect(url_for("profile", username=session["user"]))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    makes = mongo.db.makes.find().sort("make", 1)
    return render_template("edit_review.html", review=review, makes=makes)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    This function will delete selected review from db and redirect
    to profile page. If user is admin it will redirect to manage
    reviews page.
    """
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    if session["user"] == "admin":
        return redirect(url_for(
            "get_manage", username=session["user"]))
    else:
        return redirect(url_for("profile", username=session["user"]))


@app.route("/get_manage")
def get_manage():
    """
    This function will find reviews in db and render to
    manage reviews page.
    """
    reviews = list(mongo.db.reviews.find())
    return render_template("manage_reviews.html", reviews=reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
