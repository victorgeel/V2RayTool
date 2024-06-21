#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import random
import requests
import time
import sys

# Printer function to print message gradually
def printer(message: str) -> None:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# Function to fetch random free V2Ray configs
def fetch_random_v2ray_configs(length: int) -> None:
    try:
        # Limit the length to 150 if specified length exceeds
        length = min(150, length)

        # Base URL to fetch subscription JSON
        base_url = "https://raw.githubusercontent.com/victorgeel/V2RayTool/main/subscription.json"

        # Make request to fetch proxies
        response = requests.get(base_url).json()

        # Extract proxy list from JSON response
        proxies = response.get("proxies", [])

        # Get random proxies from the list
        random_proxies = random.sample(proxies, k=length)

        # Save random proxies to a file
        if random_proxies:
            with open("data/free_v2ray.txt", "a") as data:
                for proxy in random_proxies:
                    data.write(proxy + "\n")
            printer(f"\33[2;32m{length} Proxies saved to data/free_v2ray.txt!\33[m")

    except Exception as ex:
        raise SystemExit(f"\33[2;31mError: {ex}\33[m")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ["-h", "--help"]:
        print(
            """
Help: python freeV2ray.py [length]
    Example to get free proxies: python freeV2ray.py 2
    Help message: python freeV2ray.py -h/--help 
            """
        )
    else:
        try:
            length = int(sys.argv[1])
            fetch_random_v2ray_configs(length)
        except ValueError:
            print("Invalid argument! Please provide a numeric length.")
        
