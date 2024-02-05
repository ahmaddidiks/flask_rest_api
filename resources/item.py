from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import itemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Items(MethodView):
  @blp.response(200, ItemSchema)
  def get(self, item_id):
    item = itemModel.query.get_or_404(item_id)
    return item
  
  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def put(self, item_data, item_id):
    item = itemModel.query.get(item_id)
    if item:
      item.price = item_data["price"]
      item.name = item_data["name"]
    else:
      item = itemModel(id=item_id, **item_data)
    
    print(item)
    db.session.add(item)
    db.session.commit()

    return item
  
  def delete(self, item_id):
    raise NotImplementedError("Deleting an item is not implemented.")

@blp.route("/item")
class ItemList(MethodView):
  @blp.response(200, ItemSchema(many=True))
  def get(self):
    return {
      "username": "admin",
      "email": "admin@localhost",
      "id": 42
    }
    # raise NotImplementedError("Listing items is not implemented.")

  @blp.arguments(ItemSchema)
  @blp.response(201, ItemSchema)
  def post(self, item_data):
    item = itemModel(**item_data)

    try:
      db.session.add(item)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occured while insertinf the item.")
    
    return item

