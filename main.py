class Hotel:
  def __init__(self, name, location, rating, total_rooms):
    self.name = name
    self.location = location
    self.rating = rating
    self.total_rooms = total_rooms

  def __repr__(self):
    return f"Hotel name : {self.name}, Location = {self.location}, Rating : {self.rating}, Total rooms : {self.total_rooms}"