#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_tuple = 0
    weight = 0

    for tup in my_list:
        total_tuple += tup[0] * tup[1]
        weight += tup[1]
# the first equation mul the tuple index value together and sum all together
# the second adds up only the weight value
    return (total_tuple / weight)
