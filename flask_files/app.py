import numpy as np
import pandas as pd
import sqlalchemy
import psycopg2
import os

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, jsonify, render_template
from itertools import *

#################################################
# Database Setup
#################################################
#engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/Youtube_project')
#conn = psycopg2.connect(engine)


#engine = create_engine('postgresql://postgres:postgres@localhost:5432/Youtube_project')
##conn = engine.connect()

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)

## Matts Method
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
db = SQLAlchemy(app)



# dialect+driver://username:password@host:port/database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/Youtube_project"
db = SQLAlchemy(app)

# Reflect database into  a new model
Base = automap_base()
# Reflect the tables
Base.prepare(db.engine, reflect=True)
# Save references to each table (table name in db HomeAnalysis)
# Metatdata = Base.classes.year_metatdata (this is a separate table in the Bellybutton hw)
#Trending = Base.classes.youtube

Base.classes.keys()

####new trial joaqiun
conn_string = "host='localhost' dbname='Youtube_project' user='postgres' password='postgres'"
    # print the connection string we will use to connect
    #print "Connecting to database\n    ->%s" % (conn_string)
    # get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (     
        render_template("index.html")
    )

# =============================================================================
# 
# @app.route("/data")
# def data():
#    sel = [
#    Base.classes.youtube.video_id,
#    Base.classes.youtube.trending_date,
#    Base.classes.youtube.category_id,
#    Base.classes.youtube.views,
#    Base.classes.youtube.category,
#    Base.classes.youtube.likes,
#    Base.classes.youtube.dislikes,
#    Base.classes.youtube.comments_count
#    ]
#    results = db.session.query(*sel).all()
#    season_data = []
#    for video_id, trending_date, category_id, views, category, likes, dislikes, comments_count  in results:
#        season_dict = {}
#        season_dict["video_id"] = video_id
#        season_dict["trending_date"] = trending_date
#        season_dict["category_id"] = category_id
#        season_dict["views"] = views
#        season_dict["category"] = category
#        season_dict["likes"] = likes
#        season_dict["dislikes"] = dislikes
#        season_dict["comments_count"] = comments_count
#        
#        season_data.append(season_dict)
#    return jsonify(season_data)
# =============================================================================
    
    #############new try
    

@app.route("/data")
def data():
   
    # execute our Query
    cursor.execute("SELECT * FROM youtube")
    # retrieve the records from the database
    records = cursor.fetchall()
    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
   # pprint.pprint(records)
    #records = tuple(records)

    return render_template('index.html',cpl = records)
    return records
#type(records)
    
# =============================================================================
# if __name__ == '__data__':
#    app.run(debug=True)
# =============================================================================
    
    # Create our session (link) from Python to the DB
   
    #session = Session(bind=engine)
    
    #inspector = inspect(engine)
    #inspector.get_table_names()
  
    #results = engine.execute ('SELECT * FROM youtube_video').fetchall()
    #results = session.query("youtube_video").all()


    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    #return (results)
    #print(inspector)
    #return (results.to_json())
    
    #session.close()
    
    #new trial
    #stmt = db.session.query(Base.classes.youtube_video).statement
    #df = pd.read_sql_query(stmt, db.session.bind)
    #return (df.to_json())
    
    #d = {'col1': [1, 2], 'col2': [3, 4]}
    #df = pd.DataFrame(data=d)
    #return (df.to_json())

if __name__ == '__main__':
    app.run(debug=True)
