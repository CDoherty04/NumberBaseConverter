"""
Created by: Charlie Doherty and Jonathan Gott
HackKU - University of Kansas
4/12/2024

Run the main function in this file to begin the program
"""
from baseconverter import base_converter
from inputhandler import input_handler

if __name__ == "__main__":

    print("Hello, welcome to our base conversion project for HackKU 2024")
    # Use input to force an input to continue
    input("Press 'enter' to continue...\n")

    in_base, out_base, in_number = input_handler()

    # If the base is the same, return the same number
    if in_base == out_base:
        print(f"Base {in_base}: {in_number}\n"
              f"Base {out_base}: {in_number}")

    else:
        # Get the output number through the base_converter
        out_number = base_converter(in_base, out_base, in_number)
        print(f"Base {in_base}: {in_number}\n"
              f"Base {out_base}: {out_number}")
