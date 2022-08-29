import pysam
import gzip
import shutil
import os


def summary():
    directory = "test_data/"

    artifact_info = "--BAM SUMMARY--"
    for bamfile in os.listdir(directory):
        if bamfile.endswith(".gz"):
            bamfilepath = os.path.abspath(directory+bamfile)
            with gzip.open(bamfilepath, 'rb') as f_in, open(bamfilepath.rsplit(".", 1)[0], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            bamfile = bamfile[:-3]

        artifact_info += '\n' + str(pysam.flagstat(directory+bamfile))

    print(artifact_info)
    return True