"""
    ECB block cipher. The English alphabet, the number of letters is 26.
    The text is encoded using the permutation matrix PM and a the INTEGER number of divisions, that evenly divide
    the text unto blocks M-i

    I define inputted text with the help of Unicode and Unicode will continue helping me, but this time doing even more,
    than before. Each letter will be transferred into INT number according to Unicode, and than each INT will be
    represented as bytes. Our range of possible numbers is between:
    97 (decimal)  = 0110 0001 (binary)
    122 (decimal) = 0111 1010 (binary)

    Based on this our length is: N = 8

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
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
    ]

# PM^-1 is needed for decoding and looks like this:
PM_1 = [
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0],
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

    # INT -> Bytes
    for i in range(len(LETTERS_IN_INT)):
        for j in range(N):

            LETTERS_IN_BYTES[i] = LETTERS_IN_INT[i]



# ***** ENCODING *****
# Data must strongly be in range of english alphabet. That's why we do the verifying
while wrong_text:
    g = [120, 99]
    f = []
    for i in range(len(g)):
        a = g[i] // 64
        b = (g[i] - 64) // 32
        c = (g[i] - 64 - 32) // 16
        # 97 - 64 - 32 = 1, 1 // 16 = 0

        if (g[i] - 64 - 32 - 16) < 0:
            d = 0

        f.append([0, a, b, c, d, e, ff, gg])
        print('ff: ', ff)
        print('gg: ', gg)
    print('f ', f)



    klartext = input('Enter a text you want to have encrypted. Text must only contain letters from english alphabet. '
                     'No spacing, exclamation points whatsoever: ')
    klartext = klartext.lower()
    check_text(klartext)

if not wrong_text:
    # sending text with data to be transferred into bytes
    letters_to_bytes(klartext)
    print(LETTERS_IN_INT)
else:
    print('Goodbye. Hope you have had fun!')

