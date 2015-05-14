__author__ = 'Simon'

'''
the following code is adapted from Fanelli et al
retrieved May 2015, available at
http://www.vision.ee.ethz.ch/~gfanelli/head_pose/head_forest.html
'''

import numpy as np
import struct


# loads a depth image and returns it in matrix form.
# returns -1 if an error occured during execution.
def loaddepthimage(p_filename):
    with open(p_filename, "rb") as f:
        byte = f.read(4)
        img_width = int.from_bytes(byte, byteorder='little')
        byte = f.read(4)
        img_height = int.from_bytes(byte, byteorder='little')
        p = 0  # le nombre de pixels traités
        depth_img = np.zeros([img_width*img_height])
        numempty = 0
        numfull = 0
        byte = f.read(4)
        while byte and p < img_width*img_height:
            # find the number of consecutive zeros to insert
            numempty = int.from_bytes(byte, byteorder='little')
            # insert the zeros
            for i in range(0, numempty):
                depth_img[p] = 0
                p += 1
            # find the number of consecutive non-zero depth values to insert
            byte = f.read(4)
            numfull = int.from_bytes(byte, byteorder='little')
            # insert the depth values
            for j in range(0, numfull):
                byte = f.read(2)
                depth_img[p] = int.from_bytes(byte, byteorder='little')
                p += 1
            # read the next set of bytes
            byte = f.read(4)
    depth_img = np.reshape(depth_img, (img_height, img_width))
    return depth_img


# loads the ground truth labels
# returns an array containing the ground truths
def loadlabels(p_filename):
    with open(p_filename, "rb") as f:
        labels = np.zeros([6])
        for i in range(0,6):
            data = f.read(4)
            labels[i] = struct.unpack('f', data)[0]
    return labels
