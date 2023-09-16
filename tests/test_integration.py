import io
import unittest
import unittest.mock

from main import main


class TestIntegration(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        return super().setUp()

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_get_input_1(self, mock_stdout):
        with open("tests/sample/output1.txt") as f:
            expected_out = f.read()
        main("tests/sample/input1.txt")
        self.assertEqual(mock_stdout.getvalue(), expected_out)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_get_input_2(self, mock_stdout):
        with open("tests/sample/output2.txt") as f:
            expected_out = f.read()
        main("tests/sample/input2.txt")
        self.assertEqual(mock_stdout.getvalue(), expected_out)
