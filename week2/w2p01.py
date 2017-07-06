import re # библиотека регулярных выражений
from scipy.spatial.distance import cosine

sourceFile = open('sentences.txt', 'r')
allWords = []  #контейнер для слов
allSentences = []  #контейнер для предложений

for line in sourceFile:
    sentence = re.split('[^a-z]', line.lower()) # разбиваем на слова
    sentence = list(filter(None, sentence)) # удаляем пустые элементы в массиве

    for word in sentence:
        allWords.append(word)

    allSentences.append(sentence)

allSentences = list(filter(None, allSentences)) # удаляем пустые элементы в массиве
uniqueWords = list(set(allWords))

wordCount = []

for i in range(len(allSentences)):
    wordCount.append([])

    for j in range(len(uniqueWords)):
        wordCount[i].append(allSentences[i].count(uniqueWords[j]))

cosineDistance = []

for i in range(1, len(wordCount)):
    distance = cosine(wordCount[0], wordCount[i])
    cosineDistance.append('{0:.3f}'.format(distance))

firstMaxElement = max(cosineDistance)
first = cosineDistance.index(firstMaxElement)
cosineDistance.remove(firstMaxElement)

secondMaxElement = max(cosineDistance)
second = cosineDistance.index(secondMaxElement) + 1

# TODO сделать нормальный вывод данных в файл, как сказано в условии
# TODO перепроверить задачу
# TODO залить ее на github.com
# TODO проверить точность first и second. На правильные ли они предложения указывают?
# TODO добавить комментарии ко всем строчкам и сделать рефакторинг
