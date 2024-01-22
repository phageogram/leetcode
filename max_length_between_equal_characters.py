#!/venv/bin/python3
def maxLengthBetweenEqualCharacters(s: str) -> int:
    current_length = 0
    max_length = 0

    length = len(s)

    for i in range(length-1):
        for j in range (length-1, i, -1):
            if s[i] == s[j]:
                current_length = j - i - 1
                max_length = max(current_length, max_length)
    
    return max_length

print(maxLengthBetweenEqualCharacters(s = 'abcda'))