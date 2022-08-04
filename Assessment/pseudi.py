import os.path
import re

'''
Make sure to put 
    #F
as a comment at the end of lines that contain a function call that don't also contain an assignment (=).
'''

python_file = 'SamuelTermTwoAssesment.py'

basic_conversion_rules = {"for": "FOR", "if": "IF", "==": "<>", "while": "WHILE", "until": "UNTIL",
                          "import": "IMPORT", "class": "DEFINE CLASS", "def": "DEFINE FUNCTION", "else:": "ELSE:",
                          "elif": "ELSEIF", "except:": "EXCEPT:", "try:": "TRY:", "pass": "PASS", "in": "IN", ":":" THEN"}
prefix_conversion_rules = { "#F": "CALL "}
advanced_conversion_rules = { "return": "RETURN", "input": "INPUT", ":":" THEN"}


def l2pseudo(to_pseudo):
    for line in to_pseudo:
        print(line[0])
        line_index = to_pseudo.index(line)
        if line[0] != "#":

            line = str(line)
            line = re.split(r'(\s+)', line)
            for key, value in prefix_conversion_rules.items():
                if key in line:
                    if not str(line[0]) == '':
                        line[0] = value + line[0]
                    else:
                        line[2] = value + line[2]
            for key, value in basic_conversion_rules.items():
                for word in line:
                    if key == str(word):
                        line[line.index(word)] = value
            for key, value in advanced_conversion_rules.items():
                for word in line:
                    line[line.index(word)] = word.replace(key, value)
            for key, value in prefix_conversion_rules.items():
                for word in line:
                    if word == key:
                        del line[line.index(word)]
            to_pseudo[line_index] = "".join(line).strip()
        else:
            to_pseudo[line_index] = ""
    return to_pseudo


def p2file(to_file):
    py_file = os.path.splitext(os.path.basename(python_file))[0]
    with open(py_file + '_pseudo.txt', 'w') as writer:
        writer.write("\n".join(to_file))


def main():
    with open(python_file, 'r+') as py_file_reader:
        file_lines = py_file_reader.readlines()
        work_file = l2pseudo(file_lines)
        p2file(work_file)


if __name__ == '__main__':
    main()