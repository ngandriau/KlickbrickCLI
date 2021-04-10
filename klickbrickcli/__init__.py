__version__ = '0.1.0'

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    args = parser.parse_args()
    name = "WORLD"
    if(args.name):
        name = args.name

    print("HELLO ", name)