import nltk
from nltk.corpus import names
import random

all_names = ([(name, 'male') for name in names.words('male.txt')] +
   [(name, 'female') for name in names.words('female.txt')])
len(all_names)

random.seed(1)
random.shuffle(all_names)

def gender_features(word):
    fem= ['a', 'anna', 'andra', 'een', 'elle', 'ella', 'essa', 'ette', 'ice', 'ina', 'ine', 'issa', 'ita', 'ique', 'lea', 'linda', 'inda', 'lyn']
    end = ''
    for ending in fem:
        if word.endswith(ending):
            end = ending
        else:
            continue
    if end == '':
        end = word[-1]
    else:
        pass        
    return {'ending': end}
    
gender_features('Mar')

featuresets = [(gender_features(n), gender) for (n, gender) in all_names]
train_names = featuresets[1000:] #the rest after the 1st 1000
devtest_names = featuresets[500:1000] #second 500
test_names = featuresets[:500] #first 500 (shuffled)
classifier = nltk.NaiveBayesClassifier.train(train_names)
print(nltk.classify.accuracy(classifier, devtest_names))

#added more endings
def gender_features(word):
    fem= ['a', 'anna', 'andra', 'een', 'elle', 'ella', 'essa', 'ette', 'ice', 'ina', 'ine', 'issa', 'ita', 'ique', 'lea', 'linda', 'inda', 'lyn', 'ana', 'enna', 'onna', 'awndra', 'ondra', 'in', 'ela', 'etta', 'iece', 'isse', 'ena', 'ene', 'ecia', 'esha', 'icia', 'iesa', 'iesha', 'issia', 'isha', 'ysha', 'yssa', 'eta', 'eeta', 'ika', 'eka', 'eca', 'ica', 'leah', 'lynda', 'ynda', 'line', 'linn', 'lynn', 'lynne', 'lyne']
    end = ''
    for ending in fem:
        if word.endswith(ending):
            end = ending
        else:
            continue
    if end == '':
        end = word[-1]
    else:
        pass        
    return {'ending': end}
    

