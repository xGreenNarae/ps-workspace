#### 프로젝트 환경

- python 3.12, unittest

---

#### 사용법

`main.py` 의 `resolver` 함수에서 문제를 처리하고 str타입의 리스트로 반환합니다.
`iter(input_lines)` 를 이용하여 `next()` 로 한 줄씩 입력값을 사용합니다.

`test.py` 파일이 `TestCases.txt` 파일에서 테스트 케이스들을 읽고 처리합니다.
각 테스트 케이스는 `======`로 구분되며, 테스트케이스의 입력과 출력은 `---`로 구분됩니다.

intellij 환경의 경우, 입력을 수동으로 테스트 하기 위해 콘솔 입력 대신에 `input.txt` 파일을 사용할 수 있습니다. `python main.py < input.txt`  

---

#### 테스트

`python test.py`
