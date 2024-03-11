# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



# write a function that takes take an array and a number,
# return true or false if that number is in the array
# ask if the array is in order
#binary search
#time complexity: O(logn)
def doesNumberExist(numbers, number):
    if len(numbers) == 0 :
        return False;
    # find the index of the middle nuimber
    midIndex = len(numbers)//2 # round down is ok
    midNumber = numbers[midIndex]
    if midNumber == number:
        return True
    elif midNumber < number:
        # use recurrion
        return doesNumberExist(numbers[midIndex + 1:], number)
    else:
        return doesNumberExist(numbers[:midIndex], number)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
