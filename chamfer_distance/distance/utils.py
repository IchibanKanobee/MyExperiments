import numpy as np

def pc_normalize(pc):
    """ pc: NxC, return NxC """
    centroid = np.mean(pc, axis=0)
    #print centroid
    pc = pc - centroid
    #print pc
    #print np.sqrt(np.sum(pc**2, axis=1))
    m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
    #print m
    pc = pc / m
    return pc

