import re
import string
import numpy as np
import Stemmer


# Функция на замену спец символов
def clearWord(word):
    return re.sub('[' + string.punctuation + ']', '', word)


class LSA:
    def __init__(self):
        self.docs = []

    # Проверка на существование матрицы
    def check_matrix(self, matrix):
        if matrix == [] or matrix[0] == []:
            return False
        else:
            return True

    # Добавить предложение
    def add_sentence(self, sentence):
        self.docs.append(sentence)

    # Удаление стоп-символов
    def stop_symbols(self, sentence):
        stop = ['-', 'еще', 'него', 'сказать', 'а', 'ж', 'нее', 'со', 'без', 'же', 'ней', 'совсем', 'более', 'жизнь',
                'нельзя', 'так', 'больше', 'за', 'нет', 'такой', 'будет', 'зачем', 'ни', 'там', 'будто', 'здесь',
                'нибудь',
                'тебя', 'бы', 'и', 'никогда', 'тем', 'был', 'из', 'ним', 'теперь', 'была', 'из-за', 'них', 'то', 'были',
                'или', 'ничего', 'тогда', 'было', 'им', 'но', 'того', 'быть', 'иногда', 'ну', 'тоже', 'в', 'их', 'о',
                'только', 'вам', 'к', 'об', 'том', 'вас', 'кажется', 'один', 'тот', 'вдруг', 'как', 'он', 'три', 'ведь',
                'какая', 'она', 'тут', 'во', 'какой', 'они', 'ты', 'вот', 'когда', 'опять', 'у', 'впрочем', 'конечно',
                'от',
                'уж', 'все', 'которого', 'перед', 'уже', 'всегда', 'которые', 'по', 'хорошо', 'всего', 'кто', 'под',
                'хоть',
                'всех', 'куда', 'после', 'чего', 'всю', 'ли', 'потом', 'человек', 'вы', 'лучше', 'потому', 'чем', 'г',
                'между', 'почти', 'через', 'где', 'меня', 'при', 'что', 'говорил', 'мне', 'про', 'чтоб', 'да', 'много',
                'раз', 'чтобы', 'даже', 'может', 'разве', 'чуть', 'два', 'можно', 'с', 'эти', 'для', 'мой', 'сам',
                'этого',
                'до', 'моя', 'свое', 'этой', 'другой', 'мы', 'свою', 'этом', 'его', 'на', 'себе', 'этот', 'ее', 'над',
                'себя', 'эту', 'ей', 'надо', 'сегодня', 'я', 'ему', 'наконец', 'сейчас', 'если', 'нас', 'сказал',
                'есть',
                'не', 'сказала']

        sentence = clearWord(sentence).lower().split()
        clear_sentence = ''
        for word in sentence:
            if word not in stop:
                clear_sentence += word + ' '
        return clear_sentence.strip()

    # Получает предложение и выдаёт это предложение, состоящее из основ слов
    def my_stemmer(self, sentence):
        stemmer = Stemmer.Stemmer('russian')
        ready = ''
        sentence = sentence.split()
        for word in sentence:
            word = stemmer.stemWord(word)
            ready += word + ' '
        return ready.strip()

    # Поиск общих слов
    def search_common_words(self, lst):
        result = []
        slov = {}
        for i in range(len(lst)):
            words = lst[i].split()
            for word in words:
                if word not in slov:
                    slov[word] = 1
                else:
                    slov[word] += 1
        keys = list(slov.keys())
        values = list(slov.values())
        for i in range(len(values)):
            if values[i] > 1 and keys[i] not in result:
                result.append(keys[i])
        return result

    # Составление матрицы
    def drawing_up_the_matrix(self, words, sentences):
        matrix = []
        for i in range(len(words)):
            matrix.append([])
            for text in sentences:
                text = text.split()
                matrix[i].append(text.count(words[i]))
        return matrix

    # Поиск ближайшего предложения
    def find_near(self, coord, other_coords):
        values = []
        for i in range(len(other_coords)):
            values.append((round(abs(coord[0] - other_coords[i][0]), 4), round(abs(coord[1] - other_coords[i][1]), 4)))
        return other_coords.index(other_coords[values.index(min(values))]) + 1


lsa = LSA()

docs = [
    'Привет, как дела, лёвушка?',
    'Привет, неопознанный лев',
    'Как арахис?',
    'Как дела?'
]

docs_copy = docs.copy()

for i in range(len(docs)):
    lsa.add_sentence(docs[i])

for i in range(len(docs)):
    docs[i] = lsa.stop_symbols(docs[i])

for i in range(len(docs)):
    docs[i] = lsa.my_stemmer(docs[i])

similar_words = sorted(lsa.search_common_words(docs))

matrix = lsa.drawing_up_the_matrix(similar_words, docs)

if matrix != []:
    U, S, Vt = np.linalg.svd(matrix)

    coord = -1 * Vt[0:2, :]
    new_coord = []

    for i in range(len(docs)):
        new_coord.append((round(coord[0][i], 4), round(coord[1][i], 4)))

    print(docs_copy[lsa.find_near(new_coord[0], new_coord[1:])])
    print(new_coord)
else:
    print('К сожалению, ничего не найдено.')
