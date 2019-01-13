import sys
import re


def read_file(_filename, encoding='utf-8'):
    with open(_filename, encoding=encoding) as _file:
        for _line in _file:
            yield _line


def check_line(_line, _pattern, _parameter):
    if _pattern.search(_line):
        return not _parameter
    return _parameter


def parsing_arguments():
    if len(sys.argv) - 1 == 2:
        _parameter = ''
        _regular = sys.argv[1]
        _filename = sys.argv[2]
    elif len(sys.argv) - 1 == 3:
        _parameter = sys.argv[1]
        _regular = sys.argv[2]
        _filename = sys.argv[3]
    else:
        raise Exception('the number of parameters must be 2 or 3')

    if _parameter == '-v':
        _parameter = True
    elif _parameter == '':
        _parameter = False
    else:
        raise Exception('invalid parameter')

    return _parameter, _regular, _filename


if __name__ == '__main__':
    try:
        parameter, regular, filename = parsing_arguments()
        regular = re.compile(regular)

        for line in read_file(filename):
            if check_line(line, regular, parameter):
                print(line)

    except Exception as e:
        print(type(e), e)
