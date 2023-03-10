# Задача 34: 
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам


def input_str_list(list_text):
    list_text = list(input().split())
    return list_text

def check_poem(list_):
    vowels = 0
    list_vowels = []
    flag = True
    answer_text = ''
    set_vowels = {'у','е','ы','а','о','э','я','и','ю','ё'}
    for phrase in list_:
        vowels = len([vowels for letter in phrase if letter in set_vowels])
        list_vowels.append(vowels)
        vowels = 0
    for i in range(len(list_vowels)-1):
        if list_vowels[i] != list_vowels[i + 1] and flag == True: 
            answer_text = 'Пам парам'
            flag = False
    if flag:
        answer_text = 'Парам пам-пам'
    return answer_text


def main(poem):
    print('введите стих для проверки: ')
    list_poem = input_str_list(poem)
    res_text = check_poem(list_poem)
    print('Ответ: ', res_text)
    return res_text

if __name__== '__main__':
    text_ = ''
    text_ = main(text_)
