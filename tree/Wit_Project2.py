
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd


# In[3]:

data_f = pd.read_csv('movie_metadata.csv')


# In[4]:

# data_f.info()


# In[5]:

cols = ['actor_1_facebook_likes'] + ['gross'] + ['budget'] + ['imdb_score'] + ['movie_facebook_likes'] + ['movie_title']
data_f = data_f[cols]


# In[6]:

print(data_f.info())


# In[7]:

# getMean is a function that has been created to obtain the mean of a set of values which has to be numerical.
def getMean(col):
    return data_f[col].mean()


# In[8]:

# getRatings is a function that obtains the rating of a certain movie, and then decides whether or not the value is
# greater than the mean to decide the output.
def getRatings(movieName):
    attribute = 'imdb_score'
    currentRating = data_f[data_f['movie_title'].str.contains(movieName)][attribute]
    return 1 if currentRating[0] > getMean(attribute) else 0


# In[9]:

# getActorLikes is a function that obtains the rating of the main actor of a certain movie, and then decides whether or
# not the value is greater than the mean to decide the output.
def getActorLikes(movieName):
    attribute = 'actor_1_facebook_likes'
    currentActor = data_f[data_f['movie_title'].str.contains(movieName)][attribute]
    return 1 if currentActor[0] > getMean(attribute) else 0


# In[10]:

# getBudget is a function that obtains the budget of a certain movie, and then decides whether or
# not the value is greater than the mean to decide the output.
def getBudget(movieName):
    attribute = 'budget'
    currentBudget = data_f[data_f['movie_title'].str.contains(movieName)][attribute]
    return 1 if currentBudget[0] > getMean(attribute) else 0


# In[11]:

# getFacebookLikes is a function that obtains the likes on facebook of a certain movie, and then decides whether or
# not the value is greater than the mean to decide the output.
def getFacebookLikes(movieName):
    attribute = 'movie_facebook_likes'
    currentFBLikes = data_f[data_f['movie_title'].str.contains(movieName)][attribute]
    return 1 if currentFBLikes[0] > getMean(attribute) else 0


# In[12]:

# getBudget is a function that obtains the gross of a certain movie, and then decides whether or
# not the value is greater than the mean to decide the output.
def getGross(movieName):
    attribute = 'gross'
    currentGross = data_f[data_f['movie_title'].str.contains(movieName)][attribute]
    return 1 if currentGross[0] > getMean(attribute) else 0


# In[14]:

# Gateway is a function that obtains all the vector with the features obtained from the tree building section.
# Then, it will look for the sections in which the system does not know what value should have. Next, it will
# infer them based on the different characteristics of the system.
def Gateway(featureClass, movieName):
    infVector = ["1","1","1","1","1","1"]
    infVector.append(getRatings(movieName))
    infVector.append(getActorLikes(movieName))
    infVector.append(getBudget(movieName))
    infVector.append(getFacebookLikes(movieName))
    infVector.append(getGross(movieName))
    # featureClass.inferencevector = infVector
    return infVector
        


# In[13]:

if __name__ == '__main__':
#     database = np.genfromtxt('movie_metadata.csv', delimiter=',')
#     database = database[1:]
     print getRatings('Avatar')
    
#     currentLine = data_f.loc[data_f['gross'] == 760505847]['movie_title']
#     print(type(currentLine))
#     print currentLine[0]


# In[ ]:
