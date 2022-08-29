import shutil
import pysam
import gzip
import os

def validate():
    directory = "test_data/"

    # unzip gz files
    for bamfile in os.listdir(directory):
        if bamfile.endswith(".gz"):
            bamfilepath = os.path.abspath(directory+bamfile)
            with gzip.open(bamfilepath, 'rb') as f_in, open(bamfilepath.rsplit(".", 1)[0], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    # validation check & generate .bai file
    for bamfile in os.listdir(directory):
        if not bamfile.endswith(".gz"):
            try:
                pysam.quickcheck(directory+bamfile)
            except Exception:
                print("%s failed sanity check." % bamfile)
                return False
            try:
                pysam.index(directory+bamfile)
            except Exception:
                print("%s failed to generate bai file." % bamfile)
                return False

    print("All files validated")
    return True
