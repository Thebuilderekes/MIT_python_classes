"""function takes a sentence and arranges each word in it alphabetically"""
def sort_sen(sentence):

    split_sentence = sentence.split(" ")
    sorted_sen = sorted(split_sentence)
    new_sen = " ".join(sorted_sen)
    return new_sen

print(sort_sen("hello how are you?"))
