import unittest
from main import resolver


def read_test_cases(filename):
    with open(filename, 'r') as file:
        test_cases = file.read().strip().split("======\n")
    return test_cases


class TestResolver(unittest.TestCase):
    def test_resolver(self):
        test_cases = read_test_cases("TestCases.txt")

        for case in test_cases:
            parts = case.strip().split("---\n")
            input_lines = parts[0].strip().split('\n')
            expected_output = parts[1].strip().split('\n')

            output = resolver(input_lines)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
