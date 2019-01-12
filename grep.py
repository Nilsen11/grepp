import sys
import re

if __name__ == '__main__':
    try:
        # check if 2 or 3 parameters
        if len(sys.argv) - 1 == 2:
            parameter = ''
            # if first parameter equal -v  --> exception. (only for 3 param use)
            if sys.argv[1] == '-v':
                raise Exception('Invalid parameter')
            else:
                regular = re.compile(sys.argv[1])
            filename = sys.argv[2]
        elif len(sys.argv) - 1 == 3:
            parameter = sys.argv[1]
            regular = re.compile(sys.argv[2])
            filename = sys.argv[3]
        else:
            raise Exception('the number of parameters must be 2 or 3')

        with open(filename) as file:
            # satisfy the condition == ''  or not satisfy == '-v':
            if parameter == '':
                for line in file:
                    if regular.findall(line):
                        print(line)
            elif parameter == '-v':
                for line in file:
                    if not regular.findall(line):
                        print(line)
            else:
                raise Exception('Invalid parameter')
    except Exception as e:
        print(type(e), e)
