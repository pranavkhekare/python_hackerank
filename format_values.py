def print_formatted(numbers):
    width = len('{:b}'.format(numbers))
    for number in range(1, numbers+1):
        decimal = int(number)
        octal = '{0:o}'.format(number)
        hexa = format(number, '2X')
        binary = '{0:b}'.format(number)
        string = str.rjust(str(decimal), width) + " " + str.rjust(str(octal), width) + " " + str.rjust(str(hexa), width) + " " + str.rjust(str(binary), width) + "\n\n"
        print(string)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
