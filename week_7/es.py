# es.py
# # Week 7's Weekly Task
# this program reads a text file and outputs the number of "e's" it contains 
# Author: Stephen Kerr

# Assumptions:
# 1. The program will accept the command line argument for the filename
# 2. The text file will contain a string of text
# 3. The program will count the number of "e's" in the text file
# 4. The program will output the number of "e's" in the text file
# 5. The program will do error handling for 3 scenarios:
    # 1. The file is not found
    # 2. The file is empty
    # 3. Any other exception
    # 4. If no command line argument is passed for the filename


# import sys module to access command line arguments
import sys


def count_es_in_file(filename):# function that counts the "e's" in the file
    try:
        # open the text file in read mode
        with open(filename, 'r') as f:
            # read the contents of the file
            text = f.read()

            # count the number of all characters in the file's text
            char_count = len(text)

            # count the number of "e's" in the file's text
            e_count = text.count("e")

        print(f'The number of \'e\'s in the file is: {e_count}.'
            f'\nWhich is {e_count / char_count * 100:.2f}% of all characters in the file.')
    except FileNotFoundError: # if the file is not found display an error message
        print(f'Error: The File "{filename}" was not found!!')
    except ZeroDivisionError: # due to calulating the percentage of "e's" in the file if we get a ZeroDivisionError this means the file is empty
        print(f'Error: The File "{filename}" is empty!!')
    except Exception as e: # catch any other exception and display the error code
        print(f'Error: {e}')


if __name__ == "__main__":
    # check if the user has entered a command line argument for the filename
    if len(sys.argv) !=2:
        print("Please enter a filename as a command line argument!!"
              "\nExample: python es.py <filename>")

    else:
        filename = sys.argv[1] # if the user has entered a command line argument for the filename set the FILENAME to the command line argument
        count_es_in_file(filename) # call the e counting function


# References:
'https://www.geeksforgeeks.org/python-sys-module/'
'https://www.geeksforgeeks.org/command-line-arguments-in-python/'
'https://www.geeksforgeeks.org/python-exception-handling/'