# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 10/24/2023
# Description: Defines bubble sort and insertion sort functions that counts the number of comparisons and the
# number of exchanges made while sorting a list and returns a tuple of the two values

def bubble_count(sort_list):
    """
    A bubble sort function that counts the number of comparisons and the number of exchanges made while sorting a list
    :param sort_list: a list to be sorted
    :return: a tuple like (comparisons, exchanges)
    """
    # initialize the compare and exchange values to 0
    compare = 0
    exchange = 0
    for pass_num in range(len(sort_list) - 1):
        for index in range(
                len(sort_list) - 1 - pass_num):  # iterates for each comparison as numbers move to sorted right side
            compare += 1
            if sort_list[index] > sort_list[
                index + 1]:  # checks to see if bigger number is before smaller, runs if true
                exchange += 1
                temp = sort_list[index]
                sort_list[index] = sort_list[index + 1]
                sort_list[index + 1] = temp
    return (compare, exchange)  # returns tuple


def insertion_count(sort_list):
    """
    An insertion sort function that counts the number of comparisons and the number
    of exchanges made while sorting a list
    :param sort_list: a list to be sorted
    :return: a tuple like (comparisons, exchanges)
    """
    compare = 0
    exchange = 0
    for index in range(1, len(sort_list)):  # list of 1 is sorted so starts at 1
        value = sort_list[index]
        pos = index - 1
        # each time this loop runs it will compare the value to the value before it, finding where it fits
        # any time the if statement runs, whether it returns true or false, a comparison is being made!
        while pos >= 0:
            compare += 1
            if sort_list[pos] > value:  # runs when the previous value exists and is larger
                exchange += 1  # all exchanges happen within the conditional if
                sort_list[pos + 1] = sort_list[pos]
                pos -= 1
            else:
                break  # once sort_list[pos] <= value, we need to insert our value
        sort_list[pos + 1] = value
    return (compare, exchange)  # return tuple when complete
