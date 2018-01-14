"""
https://www.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/
"""

user_input = input("Enter a number: ")  # user input in decimal integer
user_input = int(user_input)
result_list = []

for i in range(user_input + 1):
    bi_str = str(bin(i)[2:])  # binary input in string
    while "11" in bi_str:
        bi_str = bi_str.replace("11", "1")  # discard more than on 1 in a row
    bi_list = bi_str.split("1")
    if len(bi_list) == 1:
        result_list.append("1")  # return 0 when the number is 0
    else:
        current_result = "1"
        for zeros in bi_list:
            if len(zeros) % 2 != 0:
                current_result = "0"
                # return 0 if odd number of 0s exists, 1 otherwise
        result_list.append(current_result)

print(", ".join(result_list))
