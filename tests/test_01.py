import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess32 as subprocess


def call_R_interface(func, *args):
    assert isinstance(args, tuple)

    call_seq = ["Rscript", "interface.R", func] + list(args)
    proc = subprocess.Popen(
        call_seq,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = proc.stdout.read().strip().decode()
    err = proc.stderr.read().strip().decode()
    proc.terminate()

    return output, err


class TestQ1(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    def test_check_no_args(self):
        output, err = call_R_interface('sample_check')
        self.assertIn("Error", err)

    @weight(1)
    def test_check0(self):
        output, err = call_R_interface('sample_check', '2')
        self.assertIn("Positive", output)

    @weight(1)
    def test_check1(self):
        output, err = call_R_interface('sample_check', '-2')
        self.assertIn("Negative", output)
