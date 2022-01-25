import magic
import glob

def doc(filename):
    # files = glob.glob(filename)
    # for file in files:
    print(magic.from_file(filename,mime=True))