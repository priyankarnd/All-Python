#import argument parser library
import argparse

#Create a parser
parser = argparse.ArgumentParser(description="Enter your first name and your last name")

#Add arguments
parser.add_argument("-f", required=True, help="First Name")  #-f flag is for first name
parser.add_argument("-l", required=True, help="Last name")   #-l flag is for last names

#Extract arguments
args = parser.parse_args()

#Send output
print("Hello {} {}".format(args.f,args.l))

