from point_cloud import PC_1D
from distance import EMD


signature1 = PC_1D.get_point_cloud_signature_1D(5, 10)

signature2 = PC_1D.get_point_cloud_signature_1D(8, 10)

distance = EMD.getEMD(signature1, signature2)

print distance

signature3 = PC_1D.get_point_cloud_signature_1D(8, 10)

distance = EMD.getEMD(signature2, signature2)
print distance


