import argparse
from hello.hello import hello_world

parser = argparse.ArgumentParser(description='Hello World with a twist, timestamp, and milliseconds.')
parser.add_argument('-r', type=int, default=1, help='A number to identify the greeting.')



if __name__ == "__main__":
    args = parser.parse_args()

    hello_world(5, args.r)