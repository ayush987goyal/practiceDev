from pyechonest import artist

bk = artist.Artist("Eminem")
print(bk.id)
print("Artists similar to " + bk.name)
for similar_artist in bk.similar:
	print(similar_artist.name)

#reverse = lambda s : s[::-1]

#print(reverse("AYUSH"))
