from django.contrib.auth.models import User
from adventure.models import Player, Room

f = open('room_names.txt', 'r')
room_names_file = f.read().split("\n")
f.close()

room_names_dict = {}
room_objects_array = []

for name in room_names_file:
    room_names_dict[f"r_{name.lower().replace(' ', '_')}"] = Room(title=name, description=name)

for room in room_names_dict:
    room_objects_array.append(room_names_dict[room])

for i in range(len(room_objects_array)):
    room_objects_array[i].save()

for i in range(len(room_objects_array) - 1):
    room_objects_array[i].connectRooms(room_objects_array[i + 1], "n")
