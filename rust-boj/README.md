#### 프로젝트 환경
- rustc, cargo 1.75.0

---

#### 사용법  
`main.rs` 의 resolver 함수에서 input_cursor를 통해 입력 값을 한 줄씩 읽어서 처리합니다.  
`output` 벡터에 결과 값을 넣어서 반환하면 됩니다.

예시  
```rust
let numbers: Vec<i32> = input_cursor.next().unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
let (a, b) = (numbers[0], numbers[1]);
output.push( (a + b).to_string() );
```
두 수가 공백으로 구분되어 입력된 케이스에서 두 수를 더한 값을 반환하는 예시입니다.  

---

#### 테스트
`cargo test` 명령어를 통해 테스트를 진행할 수 있습니다.
