"""
https://www.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/
[2018-01-15] Challenge #347 [Easy] How long has the light been on?
"""


def lighton_length(aString):
    str_list = aString.split("\n")  # make each line into list
    list_list = []
    for num_str in str_list:
        list_list.append(num_str.split(" "))  # make each item into list
    range_list = []
    for num_list in list_list:
        # make each small list of start/end into range of hours
        range_list.append(range(int(num_list[0]), int(num_list[1])))
    hour_list = []
    for hours in range_list:
        try:
            for hour in hours:
                if hour not in hour_list:
                    hour_list.append(hour)
                    # if there are more than one hour, break it into pieces
        except Exception:
            if hours not in hour_list:
                hour_list.append(hours)  # collect single hours directly

    return len(hour_list)


example = "6 8\n5 8\n8 9\n5 7\n4 7"
print(lighton_length(example))
