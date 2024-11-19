import sys
#sys.path.append("../")

#from utils import file_op
#import os
import psycopg2

#DATA_DIR = "/raid/data/tinkercad/signatures/pointnet-autoencoder"

#files = file_op.get_only_files(DATA_DIR)
#count = len(files)

#for i in range (count):
#    files[i] = os.path.join(DATA_DIR, files[i])

a = ["1", "2", "3"]

conn = psycopg2.connect("host=localhost dbname=tinkercad user=postgres password=tinkercad")
cur = conn.cursor()


#files = file_op.get_only_files(DATA_DIR)
#count = len(files)
count = len(a)

for i in range (count):
#    name, _ = os.path.splitext(files[i])
#    files[i] = os.path.join(DATA_DIR, files[i])
#    cur.execute("INSERT INTO assets VALUES (%s, %s, %s, %s)", (10, 'hello@dataquest.io', 'Some Name', '123 Fake St.'))
#    print name

    cur.execute("INSERT INTO tc_core.test(name) VALUES (%s)", (a[i]))

conn.commit()
cur.close()
conn.close()



