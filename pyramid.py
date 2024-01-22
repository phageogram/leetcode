#!/venv/bin/python3
def decode(message_file):
    # read the input file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Create a dictionary that maps number values to their corresponding words
    my_dict = {}

    for line in lines:
        elements = line.split()
        # Make sure the line contains at least two elements
        if len(elements) >= 2:
            key = elements[0]
            value = elements[1]
            my_dict[key] = value

    # Separate numbers from string values and store numbers in new variable
    split_lines = [line.split() for line in lines]
    numbers = sorted([int(element[0]) for element in split_lines])

    # Initialize new list to store lines in pyramid structure
    pyramid = []
    column_length = 0

    # Organize values in pyramid variable, where the length of each line is one longer than the last
    while len(numbers) > 0:
        column_length = column_length + 1
        pyramid.append(numbers[:column_length])
        numbers = numbers[column_length:]
    print(pyramid)
    # Decode the last element of each line using list comprehension and combine into a single string
    decoded_message = ' '.join([my_dict.get(str(line[-1]), '0') for line in pyramid])

    return decoded_message

print(decode("coding_qual_input.txt"))