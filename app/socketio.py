
from app import app, db
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

async_mode = None
socketio = SocketIO(app, async_mode=async_mode, engineio_logger=True, ping_timeout=5000, ping_interval=5000)
