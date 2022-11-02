def get_count_char(str_):
    empty_dict = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for letters in str_:
        if letters.isalpha() is True:
            if letters in empty_dict:
                empty_dict[letters] += 1
            else:
                empty_dict[letters] = 1
    return empty_dict

    def dict_procent(dict={}):
        total_count = sum(dict.values())
        for letter, number_ in dict.items():
            num = number_ / total_count * 100
            dict[letter] = round(num, 2)
        return dict

main_str = """Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
final = get_count_char(main_str)
print(final)
