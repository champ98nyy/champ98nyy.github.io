import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import math

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///isil.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Declare a variable to store the current session's user id
    user_id = session["user_id"]

    # Declare a variable to store the current user's username
    username = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]["username"]

    # TODO: Display the entries in the database on index.html
    rows = db.execute("SELECT * FROM concerts WHERE user_id = ? ORDER BY date DESC", user_id)

    concerts = []

    for row in rows:
        concerts.append({
            "date": row["date"],
            "artist": row["artist_name"],
            "venue": row["venue_name"],
            "city": row["city_name"],
            "state": row["state"]
        })

    return render_template("index.html", username=username, concerts=concerts)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Declare a variable to store the stock symbol & qty of shares the user wants to purchase
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate shares qty (must be whole number greater than 0)
        if not shares.isdigit():
            return apology("Invalid Quantity", 400)

        shares = int(shares)

        if shares < 1:
            return apology("Invalid Quantity", 400)

        # Validate stock symbol. If valid symbol, continue transaction process
        if lookup(symbol) == None:
            return apology("Invalid Symbol", 400)

        else:
            # Declare a variable to store the company name for the stock symbol
            company = lookup(symbol)["name"]

            # Declare a variable to store the current price of the stock
            price = (lookup(symbol)["price"])

            # Multiply the price by qty of shares user requested to buy. Set equal to total_cost variable
            total_cost = float(price*shares)

            # Determine if user has enough cash in their account to cover the purchase
            # Declare a variable to store the current session's user
            user_id = session["user_id"]

            # Declare a variable to store how much money the user has available to spend
            # SQL Query the cash value from ther user table
            cash = float(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])

            # Compare the user's current money against the total cost of the pending transaction
            # If the user can afford to complete the transaction
            if cash >= total_cost:

                # Query database to check if user already owns shares of the stock they are attempting to purchase
                own = db.execute("SELECT symbol FROM stocks WHERE id = ?", user_id)

                # Previous query returns a list of key:value dictionaries.
                # Loop through each dictionary, checking the value of the symbol for each
                # This will return a list of those values (all symbols the user currently owns shares of stock in)
                own = [x["symbol"] for x in own]

                # If the user already owns shares of the stock, add the new purchase to the existing row in the table
                if symbol in own:
                    currentshares = int(db.execute("SELECT shares FROM stocks WHERE id = ? AND symbol = ?", user_id, symbol)[0]["shares"])
                    totalshares = shares + currentshares

                    # Complete transaction by updating users stock table to reflect new total of shares
                    db.execute("UPDATE stocks SET shares = ? WHERE id = ? AND symbol = ?", totalshares, user_id, symbol)

                else:
                    # Otherwise, complete transaction by adding a new row to the stocks table to include the completed transaction
                    db.execute("INSERT INTO stocks (id, symbol, company, shares) VALUES(?, ?, ?, ?)", user_id, symbol, company, shares)

                # Update the user's current money by subtracting the total cost of the transaction from their previous money total
                cash -= total_cost

                # Update the user's money total in the users database
                db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

                # Add transaction to a new row in the user's history table
                db.execute("INSERT INTO history (user_id, symbol, company, price, shares, transaction_total, transaction_type) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, symbol, company, usd(price), shares, usd(total_cost), "Purchased")

                # Flash alert to confirm purchase
                if shares > 1:
                    flash("Your purchase of " + str(shares) + " shares of " + company + " (" + symbol + ") for " + str(usd(total_cost)) + " has been completed.")
                else:
                    flash("Your purchase of " + str(shares) + " share of " + company + " (" + symbol + ") for " + str(usd(total_cost)) + " has been completed.")

            else:
                return apology("Insufficient Funds To Complete Transaction", 403)

        # Return user to index page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Declare a variable to store the current session's user
    user_id = session["user_id"]

    # TODO: Display the entries in the database on index.html
    transactions = db.execute("SELECT symbol, company, price, shares, transaction_total, transaction_datetime, transaction_type FROM history WHERE user_id = ? ORDER BY transaction_datetime DESC", user_id)
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE upper(username) = ?", request.form.get("username").upper())

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/search", methods=["GET", "POST"])
@login_required
def search():
    """Get search results."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Declare a variable to store the stock symbol the user wants a quote for
        search = request.form.get("search")

        # Declare a variable to store the results of calling the lookup function on the stock symbol submitted by user
        results = lookup(search)


        row_number = 1
        #for row in results:
        #    print(row_number, row["eventDate"])
        #    row_number += 1

        shows = []
        for row in results:

            shows.append({
            "date": row["eventDate"],
            "artist": (row["artist"])["name"],
            "venue": (row["venue"])["name"],
            "city": ((row["venue"])["city"])["name"],
            "state": ((row["venue"])["city"])["state"],
            "country": (((row["venue"])["city"])["country"])["name"]
            })


        # Ensure symbol is valid, then display requested results
        if results == None:
            return apology("Search came up empty", 400)

      # User reached route via GET (as by clicking a link or via redirect)
        else:
            return render_template("searched.html", shows=shows)

  # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("search.html")


#@app.route("/add_show", methods=["POST"])
#@login_required
#def add_show():

#    if request.method == "POST":




@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Declare a variable for each piece of data submitted in the form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        zip_code = request.form.get("zip_code")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure password matches password confirmation
        elif password != confirmation:
            return apology("password confirmation must match password", 400)

        elif not zip_code:
            return apology("must provide zip code", 400)

        # Query database to check if username already exists
        rows = db.execute("SELECT * FROM users WHERE upper(username) = ?", username.upper())

        # If the username already exists, return an error
        if len(rows) > 0:
            return apology("username already exists", 400)

        # Otherwise, register new user by hashing their password and adding them to database
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, password, zip_code) VALUES(?, ?, ?)", username, hashed_password, zip_code)

        # Return newly registered user to login page
        return redirect("/login")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Declare a variable to store the stock symbol & qty of shares the user wants to sell
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Validate stock symbol. If valid symbol, continue transaction process
        if lookup(symbol) == None:
            return apology("Invalid Symbol", 400)

        # Validate requested qty of shares to sell is a positive integer. If valid, continue transaction process
        if shares < 1:
            return apology("Invalid quantity of shares", 400)

        # Declare a variable to store the current session's user
        user_id = session["user_id"]

        # Declare a variable to store how much money the user has available in their account
        # SQL Query the cash value from ther user table
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # Query database to check if user already owns shares of the stock they are attempting to sell
        own = db.execute("SELECT symbol FROM stocks WHERE id = ?", user_id)

        # Previous query returns a list of key:value dictionaries.
        # Loop through each dictionary, checking the value of the symbol for each
        # This will return a list of those values (all symbols the user currently owns shares of stock in)
        own = [x["symbol"] for x in own]

        # If the user currently owns shares of the stock, subtract the qty of shares they would like to sell from the qty of shares they own to determine their new total shares after the sale is completed
        if symbol in own:
            currentshares = int(db.execute("SELECT shares FROM stocks WHERE id = ? AND symbol = ?", user_id, symbol)[0]["shares"])

            totalshares = currentshares - shares

            # Ensure that user is not attempting to sell more shares than they currently own
            if totalshares < 0:
                return apology("You are attempting to sell more shares than you own. Please revise your transaction and try again.", 400)

            else:
                # Continue with requested sale of shares

                # Declare a variable to store the company name for the stock symbol
                company = lookup(symbol)["name"]

                # Declare a variable to store the current price of the stock
                price = float((lookup(symbol)["price"]))

                # Multiply the price by qty of shares user requested to sell. Set equal to total_sale variable
                total_sale = float(price*shares)

                # Update the user's current money by adding the total sale of the transaction to their previous money total
                cash = cash + total_sale

                # Complete transaction by updating users stock table to reflect new total of shares
                db.execute("UPDATE stocks SET shares = ? WHERE id = ? AND symbol = ?", totalshares, user_id, symbol)

                # Update the user's money total in the users database
                db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

                # Add transaction to a new row in the user's history table
                db.execute("INSERT INTO history (user_id, symbol, company, price, shares, transaction_total, transaction_type) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, symbol, company, usd(price), shares, usd(total_sale), "Sold")

                # Flash alert to confirm sale
                if shares > 1:
                    flash("Your sale of " + str(shares) + " shares of " + company + " (" + symbol + ") for " + str(usd(total_sale)) + " has been completed.")
                else:
                    flash("Your sale of " + str(shares) + " share of " + company + " (" + symbol + ") for " + str(usd(total_sale)) + " has been completed.")

                # Remove stock from user's portfolio if they no longer own any shares
                if totalshares == 0:
                    db.execute("DELETE FROM stocks WHERE id = ? AND symbol = ?", user_id, symbol)

        # Return user to index page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Declare a variable to store the current session's user
        user_id = session["user_id"]

        # Query database to check if user already owns shares of the stock they are attempting to sell
        own = db.execute("SELECT symbol FROM stocks WHERE id = ? ORDER BY symbol ASC", user_id)

        # Ensure that the user currently owns stock shares to sell.
        if not own:
            return apology("You do not own shares of any stocks currently.", 400)

        # Previous query returns a list of key:value dictionaries.
        # Loop through each dictionary, checking the value of the symbol for each
        # This will return a list of those values (all symbols the user currently owns shares of stock in)
        own = [x["symbol"] for x in own]

        return render_template("sell.html", own=own)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)