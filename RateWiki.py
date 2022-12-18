import urllib.request
import json
import re


def getTextWikiArticle(topic):  
    contents = urllib.request.urlopen("https://en.wikipedia.org/w/api.php?action=parse&prop=text&format=json&page="+topic).read().decode()
    parsed = json.loads(contents)

    return str(parsed.get('parse').get('text').get('*')).lower()

def countWords(text):
    worstCount = len(re.findall(r'[^a-z]worst[^a-z]', text))
    goodCount = len(re.findall(r'[^a-z]good[^a-z]', text))
    badCount = len(re.findall(r'[^a-z]bad[^a-z]', text))
    bestCount = len(re.findall(r'[^a-z]best[^a-z]', text))

    return [worstCount, goodCount, badCount, bestCount]
    
def calculateSentScore(counts):
    score = (-3)*counts[0]-counts[2]+counts[1]+3*counts[3]

    return score 
    
def getSentimentScore(topic):
    text = getTextWikiArticle(topic)
    counts = countWords(text)
    return calculateSentScore(counts)  

# Код предлагает ввести тему, а затем вызовет функцию getSentimentScore, чтобы получить оценку тональности для этой темы. 
# После, он напечатает оценку настроений.

 if __name__ == '__main__':
    topic = input("Enter a topic: ")
    sentiment_score = getSentimentScore(topic)
    print("Sentiment score for the topic '" + topic + "' is: " + str(sentiment_score))
    
# Код для обработки исключений, которые могут возникнуть при вызове API или анализе ответа API.

if __name__ == '__main__':
    try:
        topic = input("Enter a topic: ")
        sentiment_score = getSentimentScore(topic)
        print("Sentiment score for the topic '" + topic + "' is: " + str(sentiment_score))
    except Exception as e:
        print("An error occurred:", e)
