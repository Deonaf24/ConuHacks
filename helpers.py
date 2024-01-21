def distance_between_points(a1, a2):
	return 1

def calculate_score(distance):
	return 1


class LobbyManager:
	def __init__(self):
		self.lobbies = {}

	def get_lobby(self, room_id):
		if room_id in self.lobbies:
			return self.lobbies[room_id]

		self.lobbies[room_id] = Lobby(room_id)
		return self.lobbies[room_id]


class Lobby:
	def __init__(self, room_id):
		self.room_id = room_id
		self.round = 0
		self.timer = 0
		self.players = []
		self.answer = None

	def join(self, username):
		# make sure no duplicates before adding
		user_exists = False
		for player in self.players:
			if player.name == username:
				user_exists = True
				break

		if not user_exists:
			self.players.append(Player(username))
			print("New user joined")

	def left(self, username):
		for player in self.players:
			if player.name == username:
				self.players.remove(player)
				print("User left lobby")
				break

	def player_guess(self, username, loc):
		player = None
		for x in self.players:
			if x.name == username:
				player = x
				break

		if player:
			player.guess(loc, self.answer)

	def get_scoreboard(self):
		# jsonify for socket
		return {player.name : player.score for player in self.players}


class Player:
	def __init__(self, name="Guest"):
		self.name = name
		self.score = 0
	
	def guess(self, user_guess, actual):
		dist = distance_between_points(user_guess, actual)
		self.score += calculate_score(dist)
		print(f"New score: {self.score}")

