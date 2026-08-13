from datetime import datetime, timezone


class Todo:
	def __init__(self, description: str, status: str, date: datetime | None = None):
		self.description = description
		self.status = status
		self.date = date or datetime.now(timezone.utc)

	def to_dict(self) -> dict:
		return {
			"desc": self.description,
			"status": self.status,
			"createdAt": self.date.isoformat(),
		}
