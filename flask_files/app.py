import numpy as np
import pandas as pd
import sqlalchemy
import psycopg2

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################
#engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/Youtube_project')
#conn = psycopg2.connect(engine)


engine = create_engine('postgresql://postgres:postgres@localhost:5432/Youtube_project')
conn = engine.connect()


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

db = SQLAlchemy(app)
#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (     
        render_template("index.html")
    )


@app.route("/data")
def data():
    # Create our session (link) from Python to the DB
   # Base.metadata.create_all(conn)
    #session = Session(bind=engine)
    
    #"""Return a list of all passenger names"""
    # Query all passengers
   # inspector = inspect(engine)
    #inspector.get_table_names()
  
    #results = engine.execute ('SELECT * FROM youtube_video').fetchall()
    #results = session.query("youtube_video").all()
    #session.close()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    #return (results)
    #print(inspector)
    #return (results.to_json())
    
    #new trial
    stmt = db.session.query(Base.classes.youtube_video).statement
    df = pd.read_sql_query(stmt, db.session.bind)
    return (df.to_json())
    
    #d = {'col1': [1, 2], 'col2': [3, 4]}
   # df = pd.DataFrame(data=d)
   # return (df.to_json())

if __name__ == '__main__':
    app.run(debug=True)
