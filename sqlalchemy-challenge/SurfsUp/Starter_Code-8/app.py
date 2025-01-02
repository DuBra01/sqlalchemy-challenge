from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

# Database Setup
engine = create_engine("sqlite:////Users/janlelie/Desktop/Git Hub Repositories/sqlalchemy-challenge/SurfsUp/Starter_Code-8/Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)  # Corrected usage

# Reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

# Calculate the date one year ago from the most recent date
most_recent_date = session.query(func.max(Measurement.date)).scalar()
one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

# Identify the most active station
active_station = (
    session.query(Measurement.station)
    .group_by(Measurement.station)
    .order_by(func.count(Measurement.station).desc())
    .first()[0]
)

# Flask Setup
app = Flask(__name__)

# Routes
@app.route("/")
def welcome():
    return (
        "Welcome to the Hawaii Climate API!<br/>"
        "Available Routes:<br/>"
        "<ul>"
        "<li>/api/v1.0/precipitation</li>"
        "<li>/api/v1.0/stations</li>"
        "<li>/api/v1.0/tobs</li>"
        "<li>/api/v1.0/&lt;start&gt;</li>"
        "<li>/api/v1.0/&lt;start&gt;/&lt;end&gt;</li>"
        "</ul>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(
        Measurement.date >= one_year_ago
    ).all()
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations_data = session.query(Station.station).all()
    stations_list = [station[0] for station in stations_data]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    temperature_data = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.station == active_station,
        Measurement.date >= one_year_ago
    ).all()
    temperature_list = [{"date": date, "temperature": tobs} for date, tobs in temperature_data]
    return jsonify(temperature_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    sel = [
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs),
    ]
    if end:
        results = session.query(*sel).filter(
            Measurement.date >= start,
            Measurement.date <= end
        ).all()
    else:
        results = session.query(*sel).filter(Measurement.date >= start).all()
    tmin, tavg, tmax = results[0]
    return jsonify({"TMIN": tmin, "TAVG": tavg, "TMAX": tmax})

if __name__ == "__main__":
    app.run(debug=True)