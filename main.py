class Hotel:
  def __init__(self, name, location, rating, total_rooms):
    self.name = name
    self.location = location
    self.rating = rating
    self.total_rooms = total_rooms
    self.rooms = []

  def __repr__(self):
    return f"Hotel name : {self.name}, Location = {self.location}, Rating : {self.rating}, Total rooms : {self.total_rooms}"

  def add_rooms(self,room):
    self.rooms.append(room)

  def check_room_availability(self, room_number : int):
    if not isinstance(room_number, int):
      raise ValueError("This is not number")
    for room in self.rooms:
      if room.number == room_number:
         if room.availability: 
          return f"Room {room.number} is available"
         else:
          return f"Room {room.number} is not available"

    return f"Room not found"

  def get_available_rooms(self):
    for room in self.rooms:
      if room.availability:
        print(f"Room {room.number} is available")

class Room:
  def __init__(self, number, type, price, availability):
    self.number = number
    self.type = type
    self.price = price
    self.availability = availability

    
hotel1 = Hotel("Hotel 1", "Location 1", 4, 10)

room1 = Room(101, "Standard", 100, True)
room2 = Room(102, "Deluxe", 150, False)
room3 = Room(103, "Deluxe", 150, True)

hotel1.add_rooms(room1)
hotel1.add_rooms(room2)
hotel1.add_rooms(room3)

print(hotel1.rooms)
print(hotel1.check_room_availability(101))  # Output: Room 101 is available
print(hotel1.check_room_availability(102))  # Output: Room 102 is not available
print(hotel1.check_room_availability(103))  # Output: Room not found
print()
hotel1.get_available_rooms()