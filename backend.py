import flask
from flask import request, url_for, render_template, redirect

from flask_socketio import SocketIO
from flask_socketio import join_room, leave_room
from flask_socketio import Namespace, emit

from helpers import Player, LobbyManager

app = flask.Flask(__name__, template_folder=".")
socketio = SocketIO(app)
mapbox_access_token = "pk.eyJ1IjoiamVyZW1pYXMyMTMiLCJhIjoiY2xybWY1OTN6MTBpMjJrcDc0c3Z1Z3RzbiJ9.JAmfJcUFTUBaoVPQ7fvTyQ"

lobby_manager = LobbyManager()

class TriviaNamespace(Namespace):
	def on_connect(self):
		print(f"Client connected to namespace: {self.namespace}")

	def on_disconnect(self):
		print(f"Client disconnected from namespace: {self.namespace}")

	def on_join(self, data):
		username = data["username"]
		room = data["room"]
		join_room(room)
		emit("message", f"{username} has joined the room.", room=room, namespace=self.namespace)
		lobby_manager.get_lobby(room).join(data)

	def on_leave(self, data):
		username = data["username"]
		room = data["room"]
		leave_room(room)
		emit("message", f"{username} has left the room.", room=room, namespace=self.namespace)
		lobby_manager.get_lobby(room).left(username)

	def on_message(self, data):
		room = data["room"]
		print(data)
		emit("message", data["message"], room=room, namespace=self.namespace)

	def on_marker(self, data):
		lobby_manager.get_lobby(data["user"]["room"]).player_guess(data["user"]["username"], data["loc"])

socketio.on_namespace(TriviaNamespace("/playsocket"))


@app.route("/<room_code>", methods=["GET","POST"])
def my_maps(room_code):
	return render_template("index.html", room_code=room_code, mapbox_access_token=mapbox_access_token)

if __name__ == "__main__":
	socketio.run(app)
