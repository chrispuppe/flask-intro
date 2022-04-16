"""Greeting Flask app."""

from random import choice

from flask import Flask, request, url_for, render_template

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

WEAKNESS = [
    'lame', 'dumb', 'weak', 'slimy', 'smelley', 'meh',
    'mediocre', 'homely', 'messy', 'dirty']


@app.route('/')
def start_here():
    """Home page."""

    return """
      <!doctype html>
        <html>
          Hi! This is the home page.
          <a href="/hello">Welcome Page</a>
        </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    
    return render_template('hello.html', AWESOMENESS=AWESOMENESS, WEAKNESS=WEAKNESS)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get('compliment')

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = request.args.get('insult')

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
