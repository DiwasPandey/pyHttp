import requests
import json
import sys


def filter_user_data(postsURL, todosURL, usersURL):
    '''
    This function makes three separate GET requests to a server and captures info on posts, todos and users' info.
    Each response object is then parsed to extract relevant info (in this case, number of post for a user, number 
    of todos for a user, and the userId for each user is extracted) and the manipulated data is printed in order.

    Arguments :

    postsURL is the url for users' posts data
    todosURL is the url for users' todos data
    usersURL is the url for users' info data

    Returns : 
    This functions does not return anything (equivalent to returning a None)
    '''

    # make GET requests to appropriate URLs
    postResponse = requests.get(postsURL)
    todoResponse = requests.get(todosURL)
    userResponse = requests.get(usersURL)

    # validate response and check for errors
    if postResponse.status_code == 200:
        posts = json.loads(postResponse.text)
    else:
        sys.exit('Status Code {}. There was an error with the request.'
                 .format(postResponse.status_code))

    if postResponse.status_code == 200:
        todos = json.loads(todoResponse.text)
    else:
        sys, exit('Status Code {}. There was an error with the request.'
                  .format(todoResponse.status_code))

    if postResponse.status_code == 200:
        users = json.loads(userResponse.text)
    else:
        sys.exit('Status Code {}. There was an error with the request.'
                 .format(userResponse.status_code))

    # initialize dict to store data featuring each user
    outputDict = {}

    # iterate through all posts to filter users' number of posts
    for post in posts:
        userId = post['userId']
        # if user already in dictionary, increment posts counter
        if userId in outputDict:
            outputDict[userId]['posts'] += 1
        # else, create a new entry for the user
        else:
            outputDict[userId] = {
                'posts': 1,
                'todos': 0
            }

    # iterate through all todos to filter users' number of todos
    for todo in todos:
        userId = todo['userId']
        # if user already in dictionary, increment todos counter
        if userId in outputDict:
            outputDict[userId]['todos'] += 1
        # else create new entry for user
        else:
            outputDict[userId] = {
                'posts': 0,
                'todos': 1
            }

    # iterate through all users to print relevent info
    for user in users:
        userId = user['id']
        if userId in outputDict:
            u_output = outputDict[userId]['posts'] * \
                outputDict[userId]['todos']
            print('{} : {}'.format(userId, u_output))
        else:
            print('{} : 0'.format(userId))
