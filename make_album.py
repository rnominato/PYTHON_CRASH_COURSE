#Fuction that get the artist name, album and optionally the numbers of tracks in a album
def make_album(artist_name, album_title, tracks=''):

	#Returning a dictionary with the data

	music_album = {"artist":artist_name, "album":album_title}

	#include the tracks if the informations is not void.

	if tracks:
		music_album['tracks'] = tracks

	return music_album

album = make_album('Pink Floyd','Time')
print(album)

album = make_album('Paralamas do Sucesso','Os Grãos','13')
print(album)

album = make_album('Charlie Brown Jr.','Transpiração Continua e Prolongada','16')
print(album)