import os

for i in range(100):
    cmd = "convert -average model_52_%03d.png model_53_%03d.png model_523_%03d.png" % (i, i, i)
    os.system(cmd)
