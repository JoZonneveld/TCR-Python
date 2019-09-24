def reverse_string(string):
    length = len(string)
    output = ''
    for i in range(len(string)):
        output += string[(length-1) - i]

    return output


def run():
    t = reverse_string('Reverse this string')
    print(t)
