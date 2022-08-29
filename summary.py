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

    # Work on this part if we have time to make visualization for the summary
    # code from https://pypi.org/project/pysamstats/0.14/
    # mybam = pysam.Samfile(artifact_files[0])
    # a = pysamstats.load_coverage(mybam, chrom='Pf3D7_01_v3', start=10000, end=20000)
    # plt.plot(a.pos, a.reads_all)
    # plot = BytesIO()
    # plt.savefig(plot, format='png')
    # artifact_information = [(
    #     '<img src = "data:image/png;base64,{}"/>'.format(
    #         b64encode(plot.getvalue()).decode('utf-8')))]
