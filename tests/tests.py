import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from torsimany import torsimany

def test_convert_example():
    infile = os.path.join(os.path.dirname(__file__), '..', 'Examples', 'loklak.json')
    with tempfile.NamedTemporaryFile() as outfile:
        torsimany.justdoit(infile, outfile.name)


