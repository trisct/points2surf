import trimesh
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('-s', '--suffix', type=str, default='xyz')
args = parser.parse_args()

x = np.load(args.input)
#pcd = trimesh.PointCloud(x)
np.savetxt(args.input[:-4] + '.' + args.suffix, x, fmt='%.8f', delimiter=' ')
