"""
This is the solution for the Homework #7: Dictionaries and Sets.

"""
import datetime

print("Assignment on Dictionaries and Sets")
SongParameters = {
    "Song": "Aanewala Pal Jane Wala Hai",  # Title of the song.
    "Artist": "Kishore Kumar",  # Singer.
    "Lyricist": "Gulzar",  # Writers of the song.
    "Movie": "Golmaal",  # Title and Language of the movie in which the song was played.
    "Language": "Hindi",  # Language of the song
    "Actor": "Amol Palekar",  # Actor who was pictured in the song.
    "DurationInSeconds": 282,
    "ReleaseDate": datetime.date(1970, 1, 1),  # Tentative date on which the song was released.
    "GrossIncome": 1234561.12  # Tentative Gross income made by the song
}


def check(Key, Value):
    result = False
    if(parameter in SongParameters.keys()):
        if(str(SongParameters[Key]) == Value):
            result = True
    else:
        print("Parameter not in the list.")
    return result

while(True):

    for key in SongParameters.keys():
            print(key, " , ", end="")
    print()

    parameter = input("Which parameter do you want to guess ? \n")
    guessValue = input("Please enter the " + parameter + " : ")
    if(check(parameter, guessValue)):
        print("Your guess is correct.")
    else:
        print("Your guess is incorrect. Exiting ..")
        break

for k, v in SongParameters.items():
    print(k, " : ", str(v))
