import sys
sys.path.append("..")

from utils import file_op
#import file_op
from os.path import join, splitext
import os
from plyfile import (PlyData, PlyElement, make2d, PlyParseError, PlyProperty)
import numpy as np
#from datetime import datetime


SOURCE_DIR = '/raid/data/chain_conversion_test'
DEST_DIR = SOURCE_DIR

POINT_COUNT = 2048
POINT_COUNT_STR = str(POINT_COUNT)


def stl_2_obj(f):
#    start = datetime.now()
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    out_file = join(DEST_DIR, name + ".obj")
    print ("Converting file " + f)
    cmd = "meshlabserver -i " + in_file + " -o " + out_file
    os.system(cmd)
#    end = datetime.now()
#    elapsed = end - start
#    print "STL to OBJ " + str(elapsed.microseconds / 1000) + " milliseconds"
    return out_file


def obj_2_pcd(f):
#    start = datetime.now()
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    out_file = join(DEST_DIR, name + ".pcd")
    print ("Converting file " + f)
    cmd = "pcl_mesh_sampling " + in_file + " " + out_file + " -n_samples " + POINT_COUNT_STR + " -no_vis_result"
    os.system(cmd)
#    end = datetime.now()
#    elapsed = end - start
#    print "\nOBJ to PCD " + str(elapsed.microseconds / 1000) + " milliseconds"
    return out_file


def pcd_2_ply(f):
#    start = datetime.now()
    name, ext = splitext(f)
    in_file = join(SOURCE_DIR, f)
    out_file = join(DEST_DIR, name + ".ply")
    print ("Converting file " + f)
    cmd = "pcl_pcd2ply -format 0 " + in_file + " " + out_file #ascii
    #    cmd = "pcl_pcd2ply -format 1 " + in_file + " " + out_file #binary
    os.system(cmd)
#    end = datetime.now()
#    elapsed = end - start
#    print "\nPCD to PLY " + str(elapsed.microseconds / 1000) + " milliseconds"
    return out_file


def load_ply_data(filename, point_num):
    plydata = PlyData.read(filename)
    pc = plydata['vertex'].data[:point_num]
    pc_array = np.array([[x, y, z] for x,y,z in pc])
    return pc_array

def ply_2_numpy(f):
    data = load_ply_data(f, POINT_COUNT)
    return data


def pc_normalize(pc):
    """ pc: NxC, return NxC """
    l = pc.shape[0]
    centroid = np.mean(pc, axis=0)
    pc = pc - centroid
    m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
    pc = pc / m
    return pc


def stl_2_pc(f):
    obj_file = stl_2_obj(f)
    pcd_file = obj_2_pcd(obj_file)
    ply_file = pcd_2_ply(pcd_file)
    num = ply_2_numpy(ply_file)
    data = pc_normalize(num)
    return data

def stl_2_ply(f):
    obj_file = stl_2_obj(f)
    pcd_file = obj_2_pcd(obj_file)
    ply_file = pcd_2_ply(pcd_file)
    return ply_file


def main(f):
#    print f
#    start = datetime.now()
    name, ext = splitext(f)
    ply_file = stl_2_ply(f)

    num = ply_2_numpy(ply_file)
    data = pc_normalize(num)


    out_file = join(DEST_DIR, name + ".txt")
    np.savetxt(out_file, data, fmt="%.5f")
#    end = datetime.now()
#    elapsed = end - start

#    print "Total elapsed time " + str(elapsed.microseconds / 1000) + " milliseconds"


if __name__ == "__main__":
    main(sys.argv[1:][0])
