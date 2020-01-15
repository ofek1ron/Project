"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Project import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='___________________________________________________________________________________',
        year=datetime.now().year,
        message='Feel free to contact me.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Album')
def Album():
    """Renders the about page."""
    return render_template(
        'PictureAlbum.html',
        title='Top 10 Most Iconic Soccer Momments From The Past Decade',
        year=datetime.now().year,
    )
