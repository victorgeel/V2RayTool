#!/usr/bin/env python3


# Imports
import requests
import time
import sys

# Gets IPs from GitHub repository
def get_ip():
    response = requests.get("https://raw.githubusercontent.com/V2RayTool/data/main/free_v2ray.txt")
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to retrieve IPs"

# Save the IPs into txt file
def save_ip():
    temp = get_ip()
    with open("ip/result.txt", "w") as file:
        file.write(temp)

    for char in "\033[2;34mResults saved in ip/result.txt\033[m\n":
        print(char, end="", flush=True)
        time.sleep(0.01)

# Run the program
if __name__ == "__main__":
    if len(sys.argv) != 1:
        if sys.argv[1] in ["-h", "--help"]:
            print(
                """
Help: python getIP.py [arguments: optional]

    for only get IPs -> python getIP.py
    for save the IPs -> python getIP.py -s
    for help message -> python getIP.py [-h, --help] 
"""
            )
        elif sys.argv[1] == "-s":
            save_ip()
        else:
            print("Invalid argument! run with -h")
    else:
        for char in "\033[2;34m" + get_ip() + "\033[m":
            print(char, end="", flush=True)
            time.sleep(0.01)

# EOF
