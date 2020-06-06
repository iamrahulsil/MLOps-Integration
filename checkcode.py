# connecting to the code file
programfile = open('/mlopsproject/program.py', 'r')
code = programfile.read()  # reading the code file

if 'keras' or 'tensorflow' in code:  # because keras or tensorflow keyword is a cmust have for a dl program
    if 'Conv2D' in code:  # beacuse if a code is of CNN conv2D layer is a must have
        print('kerasCNN')
    else:
        print('not kerasCNN')
else:
    print('not deep learning')
