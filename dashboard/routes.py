from flask import Blueprint, jsonify
from db.models import get_session, UserMemory
from dashboard.system_info import get_system_status

api = Blueprint("api", __name__)

@api.route("/users")
def users():
    session = get_session()
    users = session.query(UserMemory).all()
    return jsonify([{"discord_id": u.discord_id, "last_updated": u.last_updated} for u in users])

@api.route("/memory/<discord_id>")
def memory(discord_id):
    session = get_session()
    user = session.query(UserMemory).filter_by(discord_id=discord_id).first()
    return jsonify({"discord_id": user.discord_id, "memory": user.memory}) if user else jsonify({})

@api.route("/system")
def system():
    return jsonify(get_system_status())
