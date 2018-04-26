# This is a file of test cases generator for cse513 final project SAT-SOLVER

import numpy as np
# lens     : number of clauses
# xnum     : number of variables
# test_num : number of test cases


def generate_CNF(lens, xnum):
    rand = np.random.randint(-1, 5, size=(xnum, lens))
    res = [[''] * lens for i in range(xnum)]
    if xnum <= 26:
        for i in range(xnum):
            s = str(chr(65+i))
            res[i] = list(np.where(rand[i] > 3,  s, ''))
            res[i] = list(np.where(rand[i] < 0, '~'+s, res[i]))
    else:
        j = 0
        x = xnum
        while x > 0:
            # for j in range(xnum/26+1):
            for i in range(26):
                s = str(chr(65 + i))
                res[i+26*j] = list(np.where(rand[i+26*j] > 3, s + str(j), ''))
                res[i+26*j] = list(np.where(rand[i+26*j] < 0, '~' + s + str(j), res[i+26*j]))
                x -= 1
                if x <= 0:
                    break
            j = j + 1
    res = np.transpose(res)

    out = []
    for i in range(lens):
        out.append(str(' '.join(res[i])))
    return out

def testcase_generator(lens, xnum, test_num):
    for i in range(test_num):
        f= open("test/testcase"+str(i)+".txt","w+")
        this_CNF = generate_CNF(lens,xnum)
        for i in range(lens):
            f.write(this_CNF[i]+"\n")