# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:45:40 2017

@author: NishitP
"""

import pickle

#function to run for prediction
def detecting_fake_news(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return prediction[0], prob[0][1]


if __name__ == '__main__':
    var = input()
    prediction, probability = detecting_fake_news(var)
    print('echo {}'.format(probability))
