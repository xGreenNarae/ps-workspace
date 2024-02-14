import subprocess

# 실행할 프로그램과 인자 설정
program = "./main"
arguments = []


# 콘솔 입력 데이터 준비
def read_test_cases(filename):
    with open(filename, 'r') as file:
        test_cases = file.read().strip().split("======\n")
    return test_cases


def assert_equal(a, b):
    assert a == b, f"Expected {b}, but got {a}"


def test_resolver():
    test_cases = read_test_cases("TestCases.txt")

    for case in test_cases:
        parts = case.strip().split("---\n")
        input_lines = parts[0].strip()
        expected_output = parts[1].strip()

        # 프로세스 실행
        result = subprocess.run([program] + arguments, input=input_lines, text=True, capture_output=True)

        # 실행 결과 비교
        assert_equal(result.stdout.strip(), expected_output)

    print("All test cases passed!")


if __name__ == "__main__":
    test_resolver()
