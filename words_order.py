#!/venv/bin/python3
def all_same(items):
    return all(x == items[0] for x in items)

def words_order(text: str, words: list) -> bool:
    split_text = text.split()

    while True:
        try:
            word_idx = [split_text.index(i) for i in words]
        except ValueError:
            return False
        break
    
    if len(word_idx) == 1:
        return True
    #if -1 in word_idx:
    #    return False
    elif all_same(word_idx) == True:
        return False
    elif sorted(word_idx) == word_idx:
        return True
    else:
        return False

print("Example:")
print(words_order("hi world im here", ["world", "here"]))

"""blah = "hi world im here"
search = ["world", "here"]
word_list = blah.split()
index = [word_list.index(i) for i in search]

print(word_list)
print(index)"""
