import os
import requests
import urllib.parse
import urllib.request

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function



def show_count(search, pg_num):
    try:

        #pg_num = f'{1}'
        url = "https://api.setlist.fm/rest/1.0/search/setlists?artistName=" + search + "&p=" + f'{pg_num}'
        #url = f"https://api.setlist.fm/rest/1.0/search/setlists?artistName="{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        headers = {"Accept": "application/json", "x-api-key": os.environ.get("API_KEY")}
        response = requests.get(url, headers=headers)
        print(response.reason)
        response.raise_for_status()
    except requests.RequestException:
        return None


    try:
        total = response.json()["total"]

        return total

    except (KeyError, TypeError, ValueError):
        return None

def lookup(search, pg_num):
    try:

        #pg_num = f'{1}'
        url = "https://api.setlist.fm/rest/1.0/search/setlists?artistName=" + search + "&p=" + f'{pg_num}'
        #url = f"https://api.setlist.fm/rest/1.0/search/setlists?artistName="{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        headers = {"Accept": "application/json", "x-api-key": os.environ.get("API_KEY")}
        response = requests.get(url, headers=headers)
        print(response.reason)
        response.raise_for_status()
    except requests.RequestException:
        return None


    try:
        #total_shows = response.json()["total"]
        data = response.json()["setlist"]
#        print("data is ", type(data))
        #return total_shows
        return data

    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"




#def lookup(search):
#    """Look up quote for symbol."""

#    headers = {
#        'Accept': 'application/json',
#        'x-api-key': os.environ.get('API_KEY'),
#    }

#    params = (
#        ('artistName', search),
#        ('p', '1'),
#        ('sort', 'sortName'),
#    )
#    url = f'https://api.setlist.fm/rest/1.0/search/artists?artistName={urllib.parse.quote_plus(search)}&p=1&sort=sortName'
    #response = requests.get('https://api.setlist.fm/rest/1.0/search/artists', headers=headers, params=params)
#    response = requests.get(url, headers=headers)





    # Contact API
#    try:
#        api_key = os.environ.get
#        url=f"https://api.setlist.fm/rest/1.0/search/artists?artistName={urllib.parse.quote_plus(search)}&p=1&sort=sortName
#        url=f"https://www.setlist.fm/search?query={urllib.parse.quote_plus(search)}/quote?token={api_key}"
#        response = requests.get(url)
#        response.raise_for_status()
#    except requests.RequestException:
#        return None

    # Parse response
#    try:
#        results=response.json()
#        return {}

#    except (KeyError, TypeError, ValueError):
#        return None




#def lookup(search):
#    requests_session = requests.Session()
#    requests_session.headers = {"Accept": "application/json", "x-api-key": os.environ.get("API_KEY")}


#    url = f"https://api.setlist.fm/rest/1.0/search?artistName={urllib.parse.quote_plus(search)}"
#    venue_name = None
#    event_date = None
#    track_names = []

#    response = requests_session.get(url)
#    results = response.json()


    #if not response.status_code == 200:
    #    return

#    print("Response is:")
#    print(response)
#    print(requests_session.headers)
#    print(results)