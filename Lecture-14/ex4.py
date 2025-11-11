def count_match(d):
    count = 0
    for k, v in d.items():
        if k == v:
            count += 1

    return count

dict_list = {
    'a': 'a',
    'c': 'c',
    'd': 'd',
    'name': 'Ekeopre'
}
result = count_match(dict_list)
print(result)
