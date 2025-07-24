def get_num_words(book_contents):
    words = book_contents.split()
    count = len(words)
    word_dict = {}
    for w in words:
        w = w.lower()
        if w not in word_dict:
            word_dict[w] = 1
        else:
            word_dict[w] += 1
    return count, word_dict

def get_character_count(book_contents):
    character_count = {}
    for c in book_contents:
        c = c.lower()
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1
    return character_count

def sort_on(item):
    return item["num"]

def get_formatted_stats(book_contents):
    sorted_dictionary = []
    for i in book_contents:
        if i.isalpha():
            sorted_dictionary.append({"char":i,"num":book_contents[i]})
    sorted_dictionary.sort(reverse=True,key=sort_on)
    return sorted_dictionary