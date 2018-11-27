# Author: Rohit Gupta
# Date: November 01, 2018
# Version 1.0


import datetime
from netmiko import ConnectHandler


def main():
    header()
    router_conn()


def header():
    print("Welcome to the programme to read XML file")
    user_name = input("Please enter your name: ")
    print("The programme was run on", datetime.datetime.now())
    print("Your interaction with the script starts {}".format(user_name))


def router_conn():
    router = {"device_type": "cisco_ios",
              "host": "192.168.44.10",
              "username": "doodleanw",
              "password": "doodleanw"
              }

    net_connect = ConnectHandler(ip=router["host"],
                                 username=router["username"],
                                 password=router["password"],
                                 device_type=router["device_type"]
                                 )
    print(net_connect)
    cli_1 = net_connect.send_command("show ip interface brief")
    print(cli_1)


if __name__ == "__main__":
    main()