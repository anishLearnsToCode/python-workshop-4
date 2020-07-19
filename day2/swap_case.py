def swapCase(string):
    # result = ''
    # for character in string:
    #     if character.isupper():
    #         result += character.lower()
    #     else:
    #         result += character.upper()

    return ''.join([character.lower() if character.isupper() else character.upper() for character in string])


print(swapCase('hello'))
print(swapCase('HEllo'))
print(swapCase('Hello World'))
