"""
    ECB block cipher. The English alphabet, the number of letters is 26.
    The text is encoded using the permutation matrix PM and a the INTEGER number of divisions, that evenly divide
    the text unto blocks M-i

    I define inputted text with the help of Unicode and Unicode will continue helping me, but this time doing even more,
    than before. Each word will be transferred into INT number according to Unicode, and than each IINt will be represented
    as bytes. Our range of possible numbers is as follows:
    97 (decimal)  = 0110 0001 (binary)
    122 (decimal) = 0111 1010 (binary)

    Based on this our length is: N = 8

    ENCODING: Ek(Mi) = Ci ==> Ci = PM x Mi
    DECODING: Dk(Ci) = Mi ==> Mi = PM^(-1) x Ci


    klartext (de) = plain text
    schluesseltext (de) = encoded text

    verschluesselungstext (de) = decoded text
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
N = 8
schluesseltext = ''

wrong_key = True
wrong_text = True

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
print(PM_1)




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


# ***** ENCODING *****
while wrong_text:
    klartext = input('Enter a text you want to have encrypted. Text must only contain '
                         'letters from english alphabet: ')

    check_text(klartext.lower())

while wrong_key:
    key = (input('Enter key for this encoding. Key must be integer: '))
    check_integer(key)


if not wrong_text and not wrong_key:
    key = int(key)
    print(3)
    print(type(key))
else:
    print('Goodbye. Hope you have had fun!')

