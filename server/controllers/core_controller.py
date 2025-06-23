from ..config import Resource, request, db, jsonify
from flask_jwt_extended import jwt_required

class CoreController(Resource):
    def __init__(self, model):
        super().__init__()
        self.Model = model

    def get(self):
        items = self.Model.query.all()

        return [item.to_dict() for item in items], 200
    
    @jwt_required()
    def post(self):
        data = request.get_json()

        try:
            valid_fields = {c.name for c in self.Model.__table__.columns}
            model_data = {k: v for k, v in data.items() if k in valid_fields}

            item = self.Model(**model_data)

            db.session.add(item)
            db.session.commit()

            return item.to_dict(), 201

        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
        
class CoreControllerOne(Resource):
    def __init__(self, model):
        super().__init__()
        self.Model = model

    def get(self, id):
        item = self.Model.query.filter_by(id=id).first()
        return item.to_dict(), 200
    
    @jwt_required()
    def patch(self, id):
        item = self.Model.query.filter_by(id=id).first()

        data = request.get_json()
        for attr, value in data.items():
            if hasattr(item, attr):
                setattr(item, attr, value)
        

        db.session.add(item)
        db.session.commit()

        return jsonify(item.to_dict()), 200
    
    @jwt_required()
    def delete(self, id):
        item = self.Model.query.filter_by(id=id).first()

        db.session.delete(item)
        db.session.commit()

        response_body = {
            'delete_successful': True,
            'message': 'No Content'
        }
        return response_body, 204

