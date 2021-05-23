import trimesh
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('-s', '--suffix', type=str, default='_np')
args = parser.parse_args()

x = np.loadtxt(args.input)
#pcd = trimesh.PointCloud(x)
np.save(args.input[:-4] + args.suffix, x)
