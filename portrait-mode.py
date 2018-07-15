from __future__ import division, print_function
import sys, os, glob, re, argparse
import numpy as np
from utils import *
from PIL import Image

def create_arg_parser():
    # Creates and returns the ArgumentParser object."""

    parser = argparse.ArgumentParser(description='Portrait Mode Effect.')
    parser.add_argument('-i', '--image', help='Path to the input file.')
    return parser

if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    file_path = parsed_args.image
    if os.path.exists(file_path):
       print("File exists.")
       img, output_file_name = execute_portrait_mode(file_path)
       img.save(output_file_name, quality=100)
       print("New image created successfully!")
