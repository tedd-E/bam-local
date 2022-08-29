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
    with open(directory+"summary.html", 'w') as summaryfile:
        summaryfile.write(artifact_info)

    with open(directory+"summary.html", 'r') as summaryfile:
        html = summaryfile.read()
        if html == EXP_HTML:
            print("matches summary output")
        else:
            print("doesnt match. kys")
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


EXP_HTML = "416648 + 0 in total (QC-passed reads + QC-failed reads)\n \
0 + 0 secondary\n\
250 + 0 supplementary\n\
0 + 0 duplicates\n\
416648 + 0 mapped (100.00% : N/A)\n\
416398 + 0 paired in sequencing\n\
209686 + 0 read1\n\
206712 + 0 read2\n\
384858 + 0 properly paired (92.43% : N/A)\n\
415559 + 0 with itself and mate mapped\n\
839 + 0 singletons (0.20% : N/A)\n\
0 + 0 with mate mapped to a different chr\n\
0 + 0 with mate mapped to a different chr (mapQ>=5)"