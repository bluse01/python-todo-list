class Todo:
  def __init__(self, name: str, description: str):
    self.name = name
    self.description = description
    
  def to_dict(self) -> dict:
    return {self.name: self.description}