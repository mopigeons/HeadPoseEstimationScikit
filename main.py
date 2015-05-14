__author__ = 'Simon'

from Utilities import *
import numpy as np


def main():
    img = loaddepthimage("frame_00003_depth.bin")
    print(img)


if __name__ == "__main__":
    main()