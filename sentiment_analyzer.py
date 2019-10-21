import re 
import tweepy 
from textblob import TextBlob
def get_sentence_sentiment(sentences): 
        ''' 
        Utility function to classify sentiment of passed sentence 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed sentence text 
        analysis = TextBlob(sentences) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            print('positive')
        elif analysis.sentiment.polarity == 0: 
            print('neutral')
        else: 
            print('negative')

sentences=input("enter yo fcking sentence, you twat  ")

get_sentence_sentiment(sentences)
def main(): 
    sentences=input("enter yo fcking sentence, you twat  ")
    get_sentence_sentiment(sentences)
    # picking positive sentences from sentences 
    psentences = [sentence for sentence in sentences if sentence['sentiment'] == 'positive'] 
    # percentage of positive sentences 
    print("Positive sentences percentage: {} %".format(100*len(psentences)/len(sentences))) 
    # picking negative sentences from sentences 
    nsentences = [sentence for sentence in sentences if sentence['sentiment'] == 'negative'] 
    # percentage of negative sentences 
    print("Negative sentences percentage: {} %".format(100*len(nsentences)/len(sentences))) 
    # percentage of neutral sentences 
    print("Neutral sentences percentage: {} %".format(100*len(sentences - nsentences - psentences)/len(sentences))) 
  
    '''#printing first 5 positive sentences 
    print("\n\nPositive sentences:") 
    for sentence in psentences[:10]: 
        print(sentence['text']) 
  
    # printing first 5 negative sentences 
    print("\n\nNegative sentences:") 
    for sentence in nsentences[:10]: 
        print(sentence['text']) '''
  
if __name__ == "__main__": 
    # calling main function 
    main() 
