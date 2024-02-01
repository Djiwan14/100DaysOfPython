from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import json

app = Flask(__name__)
# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
# If database is not in the same folder we should include its absolute location
db_path = 'C:/Users/Shokhrukh N/Desktop/PycharmProjects/Python Web Programming/Flask BackEnd/66Day/instance/cafes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route('/random')
def get_random_cafe():
    selected_cafe = db.session.execute(db.select(Cafe))
    all_cafes = selected_cafe.scalars().all()
    random_cafe = random.choice(all_cafes)

    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })


@app.route('/all')
def all():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route('/search')
def search():
    loc = request.args.get('location')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    all_cafes = result.scalars().all()
    locations = [cafe.to_dict() for cafe in all_cafes]
    if not all_cafes:
        return jsonify({"error":{"Not Found": "Sorry, we don't have a cafe at that location."}})
    else:
        return jsonify(locations=locations)

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    selected_cafe = db.get_or_404(Cafe, cafe_id)
    if selected_cafe:
        selected_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success={"success": "Successfully updated the price"})
    else:
        return jsonify(error={"error": {"Sorry a cafe wuth that id was not found in the database."}})


# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key = request.args.get('api_key')
    if api_key == "TopSecretAPIKey":
        cafe_to_delete = db.get_or_404(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(result = {"success": "Successfully deleted the cafe"})
        else:
            return jsonify(error={"error": {"Sorry a cafe with that id was not found in the database."}})
    else:
        return jsonify(error={"Forbidden": {"Please enter valis API Key"}})

if __name__ == '__main__':
    app.run(debug=True)
