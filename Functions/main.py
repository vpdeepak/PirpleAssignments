"""
This is the solution for the Homework #1: Variables.

This file displays the various attributes of my favorite song.
The different attributes are explained as and when they are defined.
"""
import datetime

print("Assignment on Functions")

def artist() :
    return "Kishore Kumar"

def movie() :
    return "Golmaal"  # Title of the movie in which the song was played.

def releaseDate() :
    return datetime.date(1970, 1 , 1) # Tentative date on which the song was released.

def isEnglishSong() :
    return False

Song = "Aanewala Pal Jane Wala Hai" # Title of the song.
Lyricist = "Gulzar" # Writers of the song.
Movie  = "Golmaal" # Title of the movie in which the song was played.
Language = "Hindi" # Language of the song
Actor = "Amol Palekar" # Actor who was pictured in the song.
DurationInSeconds = 282
GrossIncome = 1234561.12 # Tentative Gross income made by the song

print("Song : ", Song)
print("Artist : ", artist())
print("Lyricist : ", Lyricist)
print("Movie : ", movie())
print("Language : ", Language)
print("Actor : ", Actor)
print("Duration In Seconds : ", DurationInSeconds)
print("Release Date : ", releaseDate())
print("Gross Income : ", GrossIncome)
print("Whether English : ", isEnglishSong())