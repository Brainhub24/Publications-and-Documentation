import argparse
from . import modules
def main():
    parser = argparse.ArgumentParser(description='Does cool stuff.')

    sequences = parser.add_argument_group(
        'Sequences Commands', 'Generates number sequences')
    dataManagement = parser.add_argument_group(
        'Data Management', 'Saves and manages files')

    sequences.add_argument(
        '-f', '--fibonacci', help='Calculates the first N numbers in the fibonacci sequence')
    sequences.add_argument(
        '-b', '--fizzbuzz', help='Calculates the first N values of the FizzBuzz sequence.')

    dataManagement.add_argument(
        '-s', '--save', help='Pass in a file path. Saves the file to the /data folder in this project.')
    dataManagement.add_argument(
        '-p', '--print', help='Prints all files saved in the /data folder', action='store_true')

    args = vars(parser.parse_args())

    if args['fibonacci']:
        modules.fibonacci(int(args['fibonacci']))
    if args['fizzbuzz']:
        modules.fizzbuzz(int(args['fizzbuzz']))
    if args['save']:
        modules.saveFile(args['save'])
    if args['print']:
        modules.printFiles()
