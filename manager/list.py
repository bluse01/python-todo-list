import json
from datetime import datetime


def format_iso_to_local(iso_string: str) -> str:
	"""parses an ISO datetime string, converts to local time, and formats it."""
	dt_utc = datetime.fromisoformat(iso_string)
	dt_local = dt_utc.astimezone()
	return dt_local.strftime("%b %d, %Y at %I:%M %p")


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

			formatted_created = format_iso_to_local(v["createdAt"])
			formatted_updated = format_iso_to_local(v["updatedAt"])

			print(
				f"id: {k} - description: {v['desc']} | status: {v['status']} | createdAt: {formatted_created} | updatedAt: {formatted_updated}"
			)

	except FileNotFoundError:
		print("Config file doesn't exist yet Create a todo first!")
	except json.JSONDecodeError:
		print("Config file is empty or corrupted")
		print("Try deleting config.json or writing new todo if the json is empty")


def main(user_input):
	read_config(user_input.status, user_input.limit)
