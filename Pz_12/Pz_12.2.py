#2. Из списка: ['Валентин', 'Пётр', 'Анна', 'Евгений',
#'Константин', 'Валерия', 'Юлия'] получить новый список, в
#котором длина слов не превышает 5 символов
name_list = ['Валентин', 'Пётр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
name_subsequence = [i for i in name_list if len(i) < 5]
print(name_subsequence)