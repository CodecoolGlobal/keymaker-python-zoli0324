import string


def shift_characters(word, shift):
    """
    >>> shift_characters('abby', 5)
    'fggd'
    """
    abc = string.ascii_lowercase
    new_letter = ""
    while  shift >= len(abc):
        shift = shift - len(abc)

    for letter in word:
        if abc.index(letter) + shift <= len(abc):
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
        pad_word += shift_characters(pad_word[-3:], shift)
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
                concatenate_string += matrix[row][col][::-1]
    return concatenate_string

        
print(zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']))   


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


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
