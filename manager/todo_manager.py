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
