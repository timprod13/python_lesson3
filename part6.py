def int_func(text):
    separate_word = text.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


print(int_func("the maintainers of pytest and thousands of other packages are working with titled to deliver "
               "commercial support and maintenance for the open source dependencies you use to build your "
               "applications save time reduce risk and improve code health while paying the maintainers of the "
               "exact dependencies you use"))
