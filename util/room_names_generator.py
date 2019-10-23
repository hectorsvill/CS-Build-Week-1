f = open('room_names.txt', 'r')
room_names = f.read().split("\n")
f.close()

room_names_map = {}

for name in room_names:
    room_names_map[f"r_{name.lower().replace(' ', '_')}"] = name

print(room_names_map)