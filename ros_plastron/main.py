import sys

from src import plastron_parser

parser = plastron_parser.getparser()

print("ROS-Plastron\n")
while True:
    try:
        parse_in = input('>>')
        parser.parse(parse_in)
    except (EOFError, KeyboardInterrupt):
        break

