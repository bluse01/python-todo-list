import json
from datetime import datetime, timezone


class Todo:
	def __init__(
		self,
		description: str,
		status: str,
		createdAt: datetime | None = None,
		updatedAt: datetime | None = None,
	):
		self.description = description
		self.status = status
		self.createdAt = createdAt or datetime.now(timezone.utc)
		self.updatedAt = updatedAt

	def to_dict(self) -> dict:
		return {
			"desc": self.description,
			"status": self.status,
			"createdAt": self.createdAt.isoformat(),
			"updatedAt": self.updatedAt.isoformat()
			if self.updatedAt is not None
			else None,
		}


class TaskManager:
	def __init__(self, file_name: str = "config.json"):
		self.file_name = file_name

	def load(self) -> dict:
		try:
			with open(self.file_name, "r") as config:
				return json.load(config)

		except FileNotFoundError:
			print("Config file doesn't exist yet Create a todo first!")
			return {}

		except json.JSONDecodeError:
			print("Config file is empty or corrupted")
			print("Try deleting config.json or writing new todo if the json is empty")
			return {}

	def save(self, data: dict) -> None:
		with open(self.file_name, "w") as config:
			json.dump(data, config)

	def delete(self, task_id: str) -> None:
		config = self.load()

		removed = config.pop(task_id, None)

		if removed is not None:
			print(f"Successfully deleted ID: '{task_id}'")
		else:
			print(f"ID: '{task_id}' was not found")

		self.save(config)

	def update_task(
		self, task_id: str, desc: str | None = None, status: str | None = None
	) -> None:
		config = self.load()

		if task_id not in config:
			print(f"Task ID '{task_id}' not found.")
			return

		if desc:
			config[task_id]["desc"] = desc

		if status:
			config[task_id]["status"] = status

		config[task_id]["updatedAt"] = datetime.now(timezone.utc).isoformat()

		self.save(config)
		print(f"Task '{task_id}' updated successfully.")
