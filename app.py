from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/blackcoffer_db'
db = SQLAlchemy(app)

class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intensity = db.Column(db.Float)
    likelihood = db.Column(db.Float)
    relevance = db.Column(db.Float)
    year = db.Column(db.Integer)
    country = db.Column(db.String(100))
    topic = db.Column(db.String(100))
    region = db.Column(db.String(100))
    city = db.Column(db.String(100))
    sector = db.Column(db.String(100))
    pestle = db.Column(db.String(100))
    source = db.Column(db.String(100))
    swot = db.Column(db.String(100))
    end_year = db.Column(db.String(100))
    insight = db.Column(db.Text)
    url = db.Column(db.Text)
    start_year = db.Column(db.String(100))
    impact = db.Column(db.String(100))
    added = db.Column(db.String(100))
    published = db.Column(db.String(100))
    title = db.Column(db.Text)

@app.route('/api/data', methods=['GET'])
def get_data():
    filters = request.args.to_dict()
    query = DataPoint.query
    for key, value in filters.items():
        query = query.filter(getattr(DataPoint, key) == value)
    return jsonify([d.__dict__ for d in query.all()])

if __name__ == '__main__':
    db.create_all()
    with open('/mnt/data/jsondata.json') as f:
        data = json.load(f)
        for entry in data:
            db.session.add(DataPoint(**entry))
        db.session.commit()
    app.run(debug=True)
