'''
# zip() in Python - The purpose of zip() is to map the similar index of multiple containers so that they can be
  used just using as single entity.
--> The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
  iterator is paired together, and then the second item in each passed iterator are paired together etc.
--> If the passed iterators have different lengths, the iterator with the least items decides the length of the
    new iterator.
# Syntax :
    zip(*iterators)
# Parameters :
    Python iterables or containers ( list, string etc )
# Return Value :
    Returns a single iterator object, having mapped values from all the containers.
'''


my_friends = ['Parosh', 'Rohit', 'Anower']
their_age = (26, 27, 28)
their_gender = ['Male', 'Male', 'Male']

their_all_info = list(zip(my_friends,their_age,their_gender))
print(their_all_info, '\n')

'''
# How to unzip?
--> Unzipping means converting the zipped values back to the individual self as they were. This is done with the 
    help of “*” operator.
'''

# Unzipping the previous zipped list.

my_friends = ['Parosh', 'Rohit', 'Anower']
their_age = [26, 27, 28]
their_gender = ['Male', 'Male', 'Male']

their_all_info = list(zip(my_friends,their_age,their_gender))
print("The zipped result: \n", end="")
print(their_all_info, '\n')
my_friendsz, their_agez, their_genderz = zip(*their_all_info)
print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(my_friendsz)

print("The roll_no list is : ", end="")
print(their_agez)

print("The marks list is : ", end="")
print(their_genderz, '\n')

'''
# Practical Applications : There are many possible applications that can be said to be executed using zip, be it 
  student database or scorecard or any other utility that requires mapping of groups. A small example of 
  scorecard is demonstrated below.
'''

# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for players, scores in zip(players,scores):
    print(f'Player Name: {players}, Score: {scores}.')