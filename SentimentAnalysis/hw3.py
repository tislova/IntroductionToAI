import json
import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

newModel = {} #Global dictionary to store sentiment scores of the words
lemmatizer = WordNetLemmatizer() #Instance of the WordNetLemmatizer to normalize words
stop_words = set(stopwords.words('english')) #Create a set of english stop words
#The function that will train a sentiment analysis model using JSON training file
def calcSentiment_train(trainingFile):
    global newModel #Declare global variable of sentimentModel
    with open(trainingFile, 'r') as trainData: #Open the JSON file to read
        for line in trainData: #Iterate over each line
            dictionary = json.loads(line) #Convert JSON line into a dictionary
            #Convert the dictionary to lowercase to provide consistency between words, which improves matching between training and testing data
            new_text = dictionary['review'].lower() 
            new_text = new_text.translate(str.maketrans('', '', string.punctuation)) #Remove punctuation to prevent issues during word splitting and get more accurate sentiment scores
            #Split the new text into words and lemmatize each one
            words = [lemmatizer.lemmatize(word) for word in new_text.split() if word not in stop_words] #Only if the word is not a stop word. 
            #Stop words do not have any sentiment meaning, so they can be removed for more efficient calculations
            label = dictionary['sentiment'] #Obtain the sentiment label(boolean value)
            for word in words: #Iterate over each word
                if word not in newModel: #If the word is not already in the model, its score should be 0
                    newModel[word] = 0
                #Update the sentiment score. If the review is positive, add one. If it is negative, subtract one.
                if label:
                    newModel[word] += 1
                else:
                    newModel[word] -= 1
    #Sort the dictionary by sentiment score in non-decreasing order
    newModel = dict(sorted(newModel.items(), key=lambda item: item[1]))
    values = list(newModel.values()) #List of all sentiment scores
    n = len(values) #The number of scores in the model
    #Calculate indices at the 10th and 90th percentile
    lower = int(n * 0.10)
    upper = int(n * 0.90)
    #Obtain values at the lower and upper threshold
    lower = values[lower]
    upper = values[upper]
    #Remove extreme words from the model that fall below the 10th percentile or above the 90th percentile
    #We do that to get more reliable information for analysis
    Model = {}
    for i, j in newModel.items():
        if lower <= j <= upper:
            Model[i] = j
    newModel = Model
    #In this part, we normalize sentiment scores to focus more on the sign of the value
    for word in newModel:
        if newModel[word] < 0:
            newModel[word] = -1
        elif newModel[word] > 0:
            newModel[word] = 1
        else:
            newModel[word] = 0
#The function that takes text as an input and determines if the text is positive(True) or negative(False)
def calcSentiment_test(text):
    text = text.lower() #Convert the input into a lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)) #Remove punctuation
    words = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words] #Split the new text into words and lemmatize each one, if it is not a stop word
    score = 0
    for word in words: #Iterate over each word
        if word in newModel: #If the word is in our trained model, update the total score
            score += newModel[word]
    if score > 0: #Return the result
        return True
    else:
        return False 