# [2018-01-22] Challenge #348 [Easy] The rabbit problem

# how long it will take for them to outnumber humans 2:1
# Every month a fertile female will have 14 offspring (5 males and 9 females).
# A female rabbit is fertile when it has reached the age of 4 months.
# Rabbits die at the age of 8 years (96 months).
# The initial rabbits will always be 2 months old.

# rabbit now = females + males
# females = (previous females 0~95) + (previous female 4~96) * 9
# male = (previous males 0~95) + (previous female 4~96) * 5

# get input
# split input into a list of numbers
# set female, male [0, initial, 0, 0, ... 0]
# set count = 0
# set death = 0
# while female + male < target:
#   fertile = sum(female[4:])
#   new_female = fertile * 9
#   new_male = fertile * 5
#   death += female[96] + male[96]
#   female[1:] = female[:96]
#   male[1:] = male[:96]
#   female[0] = new_female
#   male[0] = new_male
#   count += 1
# return (count, death)


def rabbit(aStr):
    initial = [int(a) for a in aStr.split(" ")]
    female, male = [[0 for i in range(96)] for j in range(2)]
    female[2] = initial[1]
    male[2] = initial[0]

    count = 0
    death = 0
    while sum(female) + sum(male) < initial[2]:
        fertile = sum(female[4:])
        female.insert(0, fertile * 9)
        dead_female = female.pop()
        male.insert(0, fertile * 5)
        dead_male = male.pop()
        count += 1
        death += dead_female + dead_male

    return count, death

print(rabbit("2 4 1000000000"))
print(rabbit("2 4 15000000000"))
