import numpy as np


if __name__ == "__main__":
    filename = 'rb2d_ra1e6_s42.npz'
    d = np.load(filename)

    for key in d.keys():
        print("Key: {}\tShape: {}\t".format(key, d[key].shape))
        print(d[key])
