import json


def read_config(target: str, limit: int):
	try:
		with open("config.json", "r") as config:
			config_parsed = json.load(config)

		if target:
			filtered_list = {
				k: v for k, v in config_parsed.items() if v["status"] == target
			}
		else:
			filtered_list = dict(config_parsed)

		for i, (k, v) in enumerate(filtered_list.items()):
			if i > limit - 1:
				break
			print(f"id: {k} - description: {v['desc']} | status: {v['status']}")

	# f"Id: {todo}, description: {filtered_list[str(todo)]['desc']}, status: {filtered_list[str(todo)]['status']}"
	except FileNotFoundError:
		print("Config file doesn't exist yet Create a todo first!")
	except json.JSONDecodeError:
		print("Config file is empty or corrupted")
		print("Try deleting config.json or writing new todo if the json is empty")


def main(user_input):
	read_config(user_input.status, user_input.limit)
