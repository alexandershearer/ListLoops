songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0], songs[2])
print(songs[1:3])

songs[0] = "Back in Black"
songs.append("Pray for Me")
songs.extend(["Righteous", "Blueberry Faygo"])
songs.insert(0, "Passionfruit")
songs.remove("Do It")
for song in songs:
    print(song)

#Animals list and loop

animals = ["Cat", "Dog", "Bird"]
animals.append("Wolf")
print(animals[2])
del animals[0]

for animal in animals:
    print(animal)