import string


def shift_characters(word, shift):
    """
    >>> shift_characters('abby', 5)
    'fggd'
    """
    abc = string.ascii_lowercase
    new_letter = ""
    while  shift >= len(abc):
        shift -= len(abc)

    for letter in word:
        if abc.index(letter) + shift < len(abc):
            new_letter += abc[abc.index(letter) + shift]
        else:
            new_letter += abc[(abc.index(letter) + shift) - len(abc)]
    return new_letter


def pad_up_to(word, shift, n):
    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    pad_word = ""
    pad_word += word
    while len(pad_word) < n:
        pad_word += shift_characters(pad_word[-len(word):], shift)
    return pad_word[0:n]


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    'zyxw'
    """
    mirrored_word = ""
    abc = string.ascii_lowercase
    start = abc[0:13]
    end = abc[13:26][::-1]
    for letter in word:
        if letter in start:
            mirrored_word += end[start.index(letter)]
        else:
            mirrored_word += start[end.index(letter)]
    return mirrored_word


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    abc = string.ascii_lowercase
    matrix = []
    for letter in word2:
        matrix.append(shift_characters(word1, abc.index(letter)))
    return matrix 


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    concatenate_string = ""

    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if col % 2 == 0:
                concatenate_string += matrix[row][col]
            else:
                concatenate_string += matrix[len(matrix) - 1 - row][col]
    return concatenate_string 


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    while n > len(word):
        n -= len(word)

    return word[-n:] + word[:-n]


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    index_chars = ""
    for index in range(len(word)):
        if pow(index, 2) < len(word):
            index_chars += word[pow(index, 2)]
    return index_chars


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    cutted_word = []
    prev_index = 0
    new_string = ""

    for index in range(block_length, len(word), block_length):
        cutted_word.append(word[prev_index: index])
        prev_index = index
    cutted_word.append(word[prev_index:])
    
    for index in range(len(cutted_word)):
        if index % 2 == 0:
            new_string += cutted_word[index]
    return new_string


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    cutted_word = word[:n]
    new_string = cutted_word[n // 3:] + cutted_word[:n // 3]
    return new_string[::-1]
    



def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
