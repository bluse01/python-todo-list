import json


def update_todo(id: str, desc: str, config: dict):
	if id in config:
		config[id]["desc"] = desc


def update_config(new_config: dict):
	with open("config.json", "w") as config:
		json.dump(new_config, config)


def read_config(target: str, desc: str):
	try:
		with open("config.json", "r") as config:
			config_parsed = json.load(config)
		update_todo(target, desc, config_parsed)
		update_config(config_parsed)

	except FileNotFoundError:
		print("Config file doesn't exist yet Create a todo first!")
	except json.JSONDecodeError:
		print("Config file is empty or corrupted")
		print("Try deleting config.json or writing new todo if the json is empty")


def main(user_input):
	read_config(user_input.id, user_input.description)
