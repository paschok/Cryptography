"""
    CAESAR cipher. The English alphabet, the number of letters is 26.
    The text is encoded using a freely chosen key of type INTEGER (for example, n = 3),
    a given letter ( X) and the division modulo the length of the alphabet. In our case - 26
    ENCODING: e(X0) = x + n mod 26
    DECODING: d(X) = X0 - n mod 26

    klartext (de) = plain text
    schluesseltext (de) = key text
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
modulo = len(alphabet) + 1
schluesseltext = ''

wrong_key = True


def check_integer(key_check):
    """
    Checking whether the input key correct is
    :param key_check:
    :return: None
    """
    global wrong_key
    try:
        if isinstance(int(key_check), int):
            wrong_key = False
    except:
        print("The number you've entered is not an integer")









klartext = input('Enter a text you want to have encrypted. Text must only contain '
                     'letters from english alphabet: ')

while wrong_key:
    key = (input('Enter key for this encoding. Key must be integer: '))
    check_integer(key)


for i in range(len(klartext)):
    print(klartext[i])
