''' The purpose of this projecct is to make a hotel class for different hotels and store a room class. can book a room and cancel it. check room, etc.
'''

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

print(hotel1)
print("Welcome to the Hotel Reservation System!")

selected_hotel = input("Enter the hotel name you want to inspect: ")

while True:
    command = input("Enter a command (check availability, book room, cancel booking,inspect other hotel, exit): ")
    command = command.lower().strip()

    if command == "check availability":
        hotel1.get_available_rooms()
    elif command == "book room":
        room_number = int(input("Enter the room number you want to book: "))
        print(hotel1.book_room(room_number))
    elif command == "cancel booking":
        room_number = int(input("Enter the room number you want to cancel the booking for: "))
        print(hotel1.cancel_book_room(room_number))
    elif command == "inspect other hotel":
      change_hotel = input("Which hotel do you want to inspect? ")
      selected_hotel = change_hotel
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")