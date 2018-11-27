# Author: Rohit Gupta
# Date: November 01, 2018
# Version 1.0

import datetime
import pprint
import xmltodict


def main():
    header()
    read_file()


def header():
    print("Welcome to the programme to read XML file")
    user_name = input("Please enter your name: ")
    print("The programme was run on", datetime.datetime.now())
    print("Your interaction with the script starts {}".format(user_name))


def read_file():
    xml_example = open("example.xml").read()
    print("Below is the XML file on which we are working on")
    print(xml_example)
    xml_dict = xmltodict.parse(xml_example)
    print(xml_dict)
    print(len(xml_dict))
    nw_details = xml_dict["interface"]["name"]["description"]
    pprint(nw_details)


if __name__ == "__main__":
    main()