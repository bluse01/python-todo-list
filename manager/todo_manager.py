class Todo:
	def __init__(self, description: str, status: str):
		self.description = description
		self.status = status

	def to_dict(self) -> dict:
		return {"desc": self.description, "status": self.status}
