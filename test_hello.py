
import unittest
from unittest.mock import patch
from io import StringIO
from hello import main


class TestHello(unittest.TestCase):
    @patch("builtins.input", return_value="Eden")
    def test_main_prints_expected_output(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as output:
            main()

        self.assertEqual(
            output.getvalue(),
            "Hello Eden\nWelcome to our project\n"
        )


if __name__ == "__main__":
    unittest.main()
