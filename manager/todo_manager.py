import json

class Todo:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    
  def to_dict(self) -> dict:
    return {self.name: self.description}