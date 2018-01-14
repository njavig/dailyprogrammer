"""
https://www.reddit.com/r/dailyprogrammer/comments/7p5p2o/20180108_challenge_346_easy_cryptarithmetic_solver/
[2018-01-08] Challenge #346 [Easy] Cryptarithmetic Solver
part 1. make the inputs into handlable source
part 2. provide an equation
part 3. put every possible cases into 2

I tried to do it with what I already know at first,
but that seems above my capacity...
so I seek some help via googling.

TBH time amount is a pain in the arse but I decided to be satisfied
with the fact that I at least make it run.
"""

import itertools


# turn a single word into specific value
def decimalizer(word, alpDic):
    result = 0
    for i in range(len(word) - 1, -1, -1):
        result += alpDic[word[i]] * 10 ** (len(word) - i - 1)
    return result


# check if the equation is correct
def calculator(lhs, rhs, alpDic):
    lhs_total = 0
    for word in lhs:
        lhs_total += decimalizer(word, alpDic)
    if lhs_total == decimalizer(rhs, alpDic):
        return True
    else:
        return False


def untangler(inputStr):
    inputList = inputStr.split(" == ")  # inputlist == ["SEND + MORE", "MONEY"]
    lhs, rhs = inputList[0], inputList[1]  # rhs == "MONEY"
    lhs = lhs.split(" + ")  # lhs == ["SEND", "MORE"]

    alpList = []
    alpDic = {}
    for char in inputStr:
        if char not in (" +=") and char not in alpList:
            alpList.append(char)  # alpList == ['S', 'E', 'N', 'D', ... 'Y']
            alpDic[char] = None  # alpDic == {'E': None, ... 'Y': None}

    # loop for every possibility and return the correct one
    options = itertools.permutations(range(10), len(alpList))
    for option in options:
        for i in range(len(alpList)):
            alpDic[alpList[i]] = option[i]
        exception = [alpDic[rhs[0]]]
        for i in range(len(lhs)):
            exception.append(alpDic[lhs[i][0]])
        if 0 not in exception:  # exception for 0-starting-word cases
            if calculator(lhs, rhs, alpDic):
                return (alpDic, "found!")  # end
            else:
                print(alpDic)  # print if the equation is not valid
        else:
            print("pass")  # print pass when any word starts with 0


print(untangler("HERE + SHE == COMES"))
