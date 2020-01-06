import os
from shutil import copy


def fibonacci(n):
    # 0th and 1st term
    nums = [0, 1]
    # Start from the 2nd term to the nth term
    for i in range(2, n + 1):
        nums.append(nums[i - 2] + nums[i - 1])
    print(nums)


def fizzbuzz(n):
    # Store our values
    nums = []
    for i in range(1, n + 1):
        val = str(i)
        if i % 3 == 0 and i % 5 == 0:
            val = 'fizzBuzz'
        elif i % 3 == 0 or i % 5 == 0:
            val = 'fizz'
        nums.append(val)
    print(nums)


def saveFile(path):
    # The location of our data directory. Will be something like C:\Users\drale\Documents\example_directory\example_package\data
    saveLoc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    # Get the file name of the passed path.
    _, fileName = os.path.split(path)

    # Get the new save location. Will be something like C:\Users\drale\Documents\example_directory\example_package\data\example.csv
    print(path)
    print(saveLoc)
    # Copy the file over
    copy(path, saveLoc)
    print('Saved!')


def printFiles():
    # The location of our data directory. Will be something like C:\Users\drale\Documents\example_directory\example_package\data
    saveLoc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    print(saveLoc)
    for file in os.listdir(saveLoc):
        # print each file
        print(file)
