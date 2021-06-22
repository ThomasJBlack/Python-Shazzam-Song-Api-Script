import requests

def requestFunc(inputPeram, endpoint):
    if endpoint == "search":
        querystring = {"term": inputPeram,
                       "locale": "en-US", "offset": "0", "limit": "10"}
    else:
        querystring = {"key": inputPeram, "locale": "en-US"}
    url = f"https://shazam.p.rapidapi.com/{endpoint}"

    headers = {
        'x-rapidapi-key': "2521c3d1a2msh56f676dd730569ep1d2672jsn3a0dd4fbd409",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    return response.json()


def printSongs(text, songList):
    print(text)
    for song in songList:  # prints out options
        index = songList.index(song)  # cant be after line 27
        if len(songList) <= 5:
            # nested data structure makes iterating of it messy
            song = song['track']
        subtitle = song['subtitle']
        name = song['title']
        print(f"({index + 1}) - {name}\n      - by {subtitle}")
