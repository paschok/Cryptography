"""
    ECB block cipher. The English alphabet, the number of letters is 26.
    The text is encoded using the permutation matrix PM and a the INTEGER number of divisions, that evenly divide
    the text unto blocks M-i, with block length N

    I define inputted text with the help of Unicode and Unicode will continue helping me, but this time doing even more,
    than before. Each letter will be transferred into INT number according to Unicode, and than each INT will be
    represented as bytes. Our range of possible numbers is between:
    97 (decimal)  = 0110 0001 (binary)
    122 (decimal) = 0111 1010 (binary)
    IMPORTANT: The highest number in english alphabet does not exceed number 128, which means, that the highest bit (128)
    will always be 0. So there is no need to implement 2 bytes, but only 1 + 7 bits. Also, the method int -> bits
    given by Python returns 7 bits, instead of 8, so based on this our length is: N = 7

    ENCODING: Ek(Mi) = Ci ==> Ci = PM x Mi
    DECODING: Dk(Ci) = Mi ==> Mi = PM^(-1) x Ci

    LETTERS_IN_INT = numbers each of which represented a SEPARATE letter using integer
    LETTERS_IN_BYTES = array of 'vectors', each of which represented a SEPARATE letter using bytes
    PM = permutation matrix

    klartext (de) = plain text
    schluesseltext (de) = encoded text

    verschluesselungstext (de) = decoded text
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
N = 8
schluesseltext = ''

wrong_text = True

LETTERS_IN_INT = []
LETTERS_IN_BYTES = []

# Permutation Matrix. 'Handmade' so that we could see what she actually is
PM = [
        [0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
    ]

# PM^-1 is needed for decoding and looks like this:
PM_1 = [
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0],
    ]


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


def letters_to_bytes(text):
    """
    Since no known to me method seems to satisfy my needs in transporting letters into bytes,
    I'll make my own method with blackjack and u Bytes.
    Way of representing INT -> Bytes: we are working only with lower case letter of eng alph. which integer equivalents
    are between 97 and 122 which means we will need 2 bytes.
    Way of transferring : division by 128, then by 64, 32, 16 and so on - this is how we receive Bytes out of string
    ATTENTION! 128 bit will always be 0, as our highest possible number is only 122
    :param text: str
    :return: nested List of INT
    """
    global LETTERS_IN_INT
    global LETTERS_IN_BYTES

    # slicing str into list of str for a better representation
    LETTERS_IN_INT = list(text)

    # converting each letter from str value into INT.
    # Ex: LETTERS_IN_INT = [120, 99]
    for i in range(len(LETTERS_IN_INT)):
        LETTERS_IN_INT[i] = ord(LETTERS_IN_INT[i])

    print('LETTERS_IN_INT: ', LETTERS_IN_INT)

    # INT -> Bytes
    for i in LETTERS_IN_INT:
        LETTERS_IN_BYTES.append([int(x) for x in list('{0:0b}'.format(i))])

    print('in bytes: ', LETTERS_IN_BYTES)

# ***** ENCODING *****
# Data must strongly be in range of english alphabet. That's why we do the verifying
while wrong_text:
    klartext = input('Enter a text you want to have encrypted. Text must only contain letters from english alphabet. '
                     'No spacing, exclamation points whatsoever: ')
    klartext = klartext.lower()
    check_text(klartext)

if not wrong_text:
    # sending text with data to be transferred into bytes
    letters_to_bytes(klartext)
else:
    print('Goodbye. Hope you have had fun!')

