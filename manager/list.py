import json


def read_config(target: str, limit: int):
	try:
		with open("config.json", "r") as config:
			config_parsed = json.load(config)
		print(config_parsed)
		for todo in range(1, len(config_parsed)):
			if todo > limit:
				break
			print(
				f"Id: {todo}, description: {config_parsed[str(todo)]['desc']}, status: {config_parsed[str(todo)]['status']}"
			)

	except FileNotFoundError:
		print("Config file doesn't exist yet Create a todo first!")
	except json.JSONDecodeError:
		print("Config file is empty or corrupted")
		print("Try deleting config.json or writing new todo if the json is empty")


def main(user_input):
	read_config(user_input.status, user_input.limit)
