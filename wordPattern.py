#!/venv/bin/python3
def wordPattern(pattern: str, s: str) -> bool:
    if len(pattern) != len(s):
        return False
    
    s_list = list(s)
    s_unique = [x for x in s_list if x not in s_unique]

    pattern_list = []
    for char in pattern:
        if char not in pattern_list:
            pattern_list.append(char)

    if len(pattern_list) != len(s_unique):
        return False

    char_mapping = {}

    for s_char, pattern_char in zip(s_unique, pattern_list):
        char_mapping[s_char] = pattern_char
        
    output_string = ""

    for key in s_unique:
        output_string += char_mapping.get(key)

    if output_string == pattern:
        return True
    
print(wordPattern("abba", "dog cat cat dog"))