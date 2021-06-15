from requestsFile import requestFunc

scriptInProgress = True

while(scriptInProgress):
    # get user input
    songInput = input("Enter a song: ")
    # send first request
    initApiResponse = requestFunc(songInput, "search")
    # process desired data from reponse

    hitsList = initApiResponse['tracks']['hits']

    # ask user to pick their song from the provided list based on its index.
    print("Enter a value coresponding to the song you entered.")
    for song in hitsList:  # prints out options
        index = hitsList.index(song)
        name = song['track']['title']
        print(f"({index}) - {name}")

    hitIndex = int(input("Value: "))

    # request and display recommended songs
    # get key to send with list-recommendations request
    key = (hitsList[hitIndex]['track']['key'])
    tracksList = requestFunc(key, "songs/list-recommendations")['tracks']

    if len(tracksList) == 0:
        print("Sorry, no recommendations.")
    else:
        print("Based on your song input, here are some songs you might like")
        for song in tracksList:
            name = song['title']
            print(name)

    # terminate script?
    scriptInProgress = int(input("Enter 0 to quit: "))
