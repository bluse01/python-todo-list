import json


def read_config(target: str):
	try:
		with open("config.json", "r") as config:
			config_parsed = json.load(config)
		print(config_parsed)
		for todo in config_parsed:
			print(
				f"Id: {todo}, description: {config_parsed[todo]['desc']}, status: {config_parsed[todo]['status']}"
			)

	except FileNotFoundError:
		print("Config file doesn't exist yet Create a todo first!")
	except json.JSONDecodeError:
		print("Config file is empty or corrupted")
		print("Try deleting config.json or writing new todo if the json is empty")


def main(user_input):
	read_config(user_input.status)
