from jikanpy import Jikan
jikan = Jikan()

def getUserCompletedList(user):

    userDict = jikan.user(username='torin99r', request='animelist',
        argument='completed')

    userCompletedDict = userDict['anime']
    listOfScores = []
    for anime in userCompletedDict:
        score = anime['score']
        listOfScores.append(score)
    print(listOfScores)
getUserCompletedList('')
