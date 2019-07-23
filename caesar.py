"""
    CAESAR cipher. The English alphabet, the number of letters is 26.
    The text is encoded using a freely chosen key of type INTEGER (for example, n = 3),
    a given letter ( X) and the division modulo the length of the alphabet. In our case - 26
    ENCODING: e(X0) = x + n mod 26
    DECODING: d(X) = X0 - n mod 26

    klartext (de) = plain text
    schluesseltext (de) = encoded text

    verschluesselungstext (de) = decoded text
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
modulo = len(alphabet) + 1
schluesseltext = ''

wrong_key = True
wrong_text = True


def check_integer(key_check):
    """
    Checking whether the input key correct is
    :param key_check: key
    :return: None
    """
    global wrong_key
    try:
        if isinstance(int(key_check), int):
            wrong_key = False
    except:
        print("The number you've entered is not an integer")


def check_text(text):
    """
    Checking whether the input text matches our condition - the alphabet.
    Lowercase english alphabet has range between 97 and 122
    :param text: klartext
    :return: None
    """
    global wrong_text
    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122:
            wrong_text = False
            continue
        else:
            wrong_text = True
            break


def find_letter_number(letter):
    """
    Finding a place of a letter in alphabet to encode
    :param letter: Str
    :return: Str
    """
    return alphabet.find(letter)


def encode(x):
    """
    Encoding: e(X0) = x + n mod 26
    :param x: int
    :return: int
    """
    global key
    global alphabet
    return (x + int(key)) % 26


def decode(x):
    """
    Decoding: e(X0) = x - n mod 26
    :param x: int
    :return: int
    """
    global key
    global alphabet
    return (x - int(key)) % 26


def find_encoding(index):
    """
    Finding the letter in a alphabet
    :param number:
    :return: Str
    """
    return alphabet[index]


# ***** ENCODING *****
while wrong_text:
    klartext = input('Enter a text you want to have encrypted. Text must only contain '
                         'letters from english alphabet: ')

    check_text(klartext.lower())

while wrong_key:
    key = (input('Enter key for this encoding. Key must be integer: '))
    check_integer(key)


if not wrong_text and not wrong_key:
    schluesseltext = ''
    for i in range(len(klartext)):
        number = encode(find_letter_number(klartext[i]))
        schluesseltext += find_encoding(number)
    print(schluesseltext)


# ***** DECODING *****
decode_desire = input('Do you wish to decode anything? y / n: ')

if decode_desire == 'y' or decode_desire == 'Y':
    wrong_key = True
    wrong_text = True

    while wrong_text:
        schluesseltext = input('Enter a text you want to have decoded. Text must only contain '
                         'letters from english alphabet: ')

        check_text(schluesseltext.lower())

    while wrong_key:
        key = (input('Enter key for this encoding. Key must be integer: '))
        check_integer(key)

    if not wrong_text and not wrong_key:
        verschluesselungstext = ''
        for i in range(len(schluesseltext)):
            number = decode(find_letter_number(schluesseltext[i]))
            verschluesselungstext += find_encoding(number)
        print(verschluesselungstext)
else:
    print('Goodbye. Hope you have had fun!')

