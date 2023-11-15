import datetime
from typing import NamedTuple

class History(NamedTuple):
  id: int
  type: str
  ammount: int
  date: any
  
  def __call__(self):
    return {
      "_id": self.id,
      "type": self.type,
      "ammount": self.ammount,
      "date": self.date
    }