from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Create Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)

class Passenger(db.Model): ##row in a db
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating
            
        }
    
with app.app_context():
    db.create_all() 


##Random routes
@app.route("/")
def home():
    return jsonify({"message": "welcome to the travel api"})


#if we have a URL and we want certain info from it like 
## https://www.thenerdnook.io/destinations we do the following 

@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = destinations.query.all()
    
    return jsonify([destination.to_dict()] for destination in destinations)

#https://www.thenerdnook.io/destinations/2 
@app.route




if __name__ == "__main__":
    app.run(debug=True) ##keeps the api running when you refresh