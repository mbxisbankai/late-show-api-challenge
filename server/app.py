from .config import app, api, jwt, Resource, jsonify
from .controllers import guest_controller, episode_controller, appearance_controller, auth_controller
from .controllers.auth_controller import Register, Login, Logout, jwt_required, get_jwt, blacklist


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in blacklist

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify({"error": "Missing or invalid Authorization header"}), 401

# Auth Routes
api.add_resource(Register, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

# Resource Routes
api.add_resource(guest_controller.GuestController, '/guests', endpoint='guests')
api.add_resource(guest_controller.GuestControllerOne, '/guests/<int:id>', endpoint='guest_by_id')

api.add_resource(episode_controller.EpisodeController, '/episodes', endpoint='episodes')
api.add_resource(episode_controller.EpisodeControllerOne, '/episodes/<int:id>', endpoint='episode_by_id')

api.add_resource(appearance_controller.AppearanceController, '/appearances', endpoint='appearances')
api.add_resource(appearance_controller.AppearanceControllerOne, '/appearances/<int:id>', endpoint='appearance_by_id')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
