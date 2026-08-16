from datetime import datetime

from manager.todo_manager import TaskManager


def format_iso_to_local(iso_string: str) -> str:
	"""parses an ISO datetime string, converts to local time, and formats it."""
	if not iso_string:
		return None

	dt_utc = datetime.fromisoformat(iso_string)
	dt_local = dt_utc.astimezone()
	return dt_local.strftime("%b %d, %Y at %I:%M %p")


def read_config(config: dict, filter_target: str, limit: int):
	if filter_target:
		filtered_list = {
			k: v for k, v in config.items() if v["status"] == filter_target
		}
	else:
		filtered_list = dict(config)

	for i, (k, v) in enumerate(filtered_list.items()):
		if i > limit - 1:
			break

		formatted_created = format_iso_to_local(v["createdAt"])
		formatted_updated = format_iso_to_local(v["updatedAt"])

		print(
			f"id: {k} - description: {v['desc']} | status: {v['status']} | createdAt: {formatted_created} | updatedAt: {formatted_updated}"
		)


def main(user_input):
	manager = TaskManager()
	config = manager.load()
	read_config(config, user_input.status, user_input.limit)
