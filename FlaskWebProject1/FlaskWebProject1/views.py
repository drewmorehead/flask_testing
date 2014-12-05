"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
#from sqlalchemy import *
from FlaskWebProject1 import app
import pygal

#engine = create_engine("mssql+pyodbc://localhost/db_4_flask?")
#metadata = metadata(bind=engine)

#cities = table('city', metadata, autoload=true)

#con = engine.connect()
#con.execute(cities.insert(), city='chicago', date='1/1/2001')

#print engine.execute('select * from cities')


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Drew''s flask app home page',
        year=datetime.now().year,
    )

@app.route('/chart')
def chart():
    """Renders a pygal chart"""
    bar_chart = pygal.HorizontalStackedBar()
    bar_chart.title = "Random barchart"
    bar_chart.x_labels = map(str, range(11))
    bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]) 
    chart = bar_chart.render(is_unicode=True)
    return render_template('chart.html', chart=chart )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Drew',
        year=datetime.now().year,
        message='Your application description page.'
    )
