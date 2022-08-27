import shutil
import pysam
import gzip
import os

def validate():
    directory = "/test_data/"

    # unzip and generate .bai
    # for bamfile in os.listdir(directory):
    #     if bamfile.endswith(".gz"):
    #         bamfilepath = os.path.abspath(bamfile)
    #         with gzip.open(bamfilepath, 'rb') as f_in, open(bamfilepath.rsplit(".",1)[0], 'wb') as f_out:
    #                 shutil.copyfileobj(f_in, f_out)
    #         bamfile = bamfile[-3:]
    #     if bamfile.endswith(".bam"):
    #         try:
    #             pysam.index(bamfile)
    #         except Exception:
    #             print("Unable to generate bai file for bam file %s" % bamfile)

    for bamfile in os.listdir(directory):
        if bamfile.endswith(".gz"):
            bamfilepath = os.path.abspath(bamfile)
            with gzip.open(bamfilepath, 'rb') as f_in, open(bamfilepath.rsplit(".", 1)[0], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            bamfile = bamfile[-3:]
        try:
            pysam.quickcheck(bamfile)
        except Exception:
            print("%s failed sanity check." %bamfile)
            return False
        os.remove(os.path.abspath(bamfile))

    return True
