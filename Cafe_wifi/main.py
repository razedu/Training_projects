from flask import Flask, render_template, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
API_KEY="secret"
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        dict = {}
        for column in self.__table__.columns:
            dict[column.name] = getattr(self, column.name)
        return dict


@app.route('/')
def home():
    cafes = db.session.query(Cafe).all()
    return render_template('index.html', cafes=cafes)


@app.route('/all')
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/random_cafe')
def random_cafe():
    cafes = choice(db.session.query(Cafe).all())
    return jsonify(cafes.to_dict())

@app.route('/price_update/<int:cafe_id>',methods=['PATCH'])
def update_price(cafe_id):
    new_price=request.args.get('new_price')
    cafe=db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price=new_price
        db.session.commit()
        return jsonify(response={'succes':'Price has been updated'})
    else:
        return jsonify(response={'error':'cafe not found'})

@app.route('/delete_cafe/<int:cafe_id>',methods=['DELETE'])
def delete_cafe(cafe_id):
    key=request.args.get('api_key')
    if key==API_KEY:
        cafe=db.session.query(Cafe).get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={'succesful':'cafe has been deleted'})
        else:
            return jsonify(response={'error':'cafe not found'})
    else:
        return jsonify(response={'error':'incorrect api_key'})


if __name__ == '__main__':
    app.run(debug=True)
