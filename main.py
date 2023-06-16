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

  def check_room_availability(self, room_number : int): #check if a room is available
    if not isinstance(room_number, int):
      raise ValueError("Room not found")
    for room in self.rooms:
      if room.number == room_number:
         if room.availability: 
          return f"Room {room.number} is available"
         else:
          return f"Room {room.number} is not available"

    return "Room not found"

  def get_available_rooms(self): #check what room is available
    for room in self.rooms:
      if room.availability:
        print(f"Room {room.number} is available")

  def book_room(self, room_number : int): #booking room
    if not isinstance(room_number, int):
      raise ValueError("Room not found")
    for room in self.rooms:
      if room.number == room_number:
        room.availability = False
    return f"Your reservation for room {room_number} is done"

  def cancel_book_room(self, room_number : int):
    if not isinstance(room_number, int):
      raise ValueError("Room not found")
    for room in self.rooms:
      if room.number == room_number:
        room.availability = True
    return f"Your cancelation for room {room.number} is done"

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

while True:
    hotel = input("What hotel do you want to inspect? ")
    command = input("Enter a command: ")
    
    if command == "check availability":
        hotel.get_available_rooms()
    elif command == "book room":
        try:
          room_number = input("Which room do you want to book? ")
        except ValueError:
          print("Please input integer")
        hotel.book_room(room_number)
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")