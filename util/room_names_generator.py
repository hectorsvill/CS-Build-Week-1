from django.contrib.auth.models import User
from adventure.models import Player, Room

f = open('room_names.txt', 'r')
room_names = f.read().split("\n")
f.close()

room_names_map = {}
room_array = []

for name in room_names:
    room_names_map[f"r_{name.lower().replace(' ', '_')}"] = Room(title=name, description=name)

for room in room_names_map:
    # room_names_map[room].save()
    room_array.append(room_names_map[room])

for i in range(len(room_array)):
    room_array[i].save()
    # room_array[i].connectRooms(room_array[i + 1], "n")

for i in range(len(room_array) - 1):
    # room_array[i].save()
    room_array[i].connectRooms(room_array[i + 1], "n")
