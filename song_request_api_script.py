from functions import requestFunc, printSongs

from os import system
_ = system('clear')  # clears the terminal/console window before each run

scriptInProgress = True

while(scriptInProgress):
    songInput = input("\nEnter a song: ")
    # send first request and access wanted data
    hitsList = requestFunc(songInput, "search")['tracks']['hits']

    # ask user to pick their song from the provided list based on its index.
    printSongs("\nSearch results:", hitsList)

    hitIndex = int(input("\nEnter a number coresponding to your song: ")) - 1

    # get key to send with list-recommendations request
    key = (hitsList[hitIndex]['track']['key'])

    # might return an empty dict
    tracksData = requestFunc(key, "songs/list-recommendations")

    if tracksData:  # makes sure the dict is not empty
        tracksList = tracksData['tracks']
        printSongs(
            "\nBased on your song, here are some songs you might like.", tracksList)
    else:  # if list is empty
        print("\nSorry, no recommendations for that song.")

    # terminate script?
    scriptInProgress = int(input("\nEnter 0 to quit or 1 to continue: "))
