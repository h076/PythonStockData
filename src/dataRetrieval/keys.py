#!/usr/bin/env python3
import tokenize

def loadAlpacaKeys(path : str) -> dict[str, str]:
    keys = {}

    try:
        with open(path) as file:
            lines = [line.strip() for line in file.readlines()]
            for line in lines:
                pair = str(line).split(":")
                keys[str(pair[0])] = str(pair[1])

            file.close()

    except FileNotFoundError:
        print("API key file not found.")

    return keys;
