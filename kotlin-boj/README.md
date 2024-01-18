`src/test/resources/TestCases.txt` 에 테스트케이스를 작성합니다.  
기본적으로 테스트케이스(입/출력쌍) 을 구분하기 위해 `======` 를 사용합니다.  
하나의 테스트케이스에서 입력과 출력을 구분하기 위해 `---` 를 사용합니다.  
이 구분 문자열은 상황에 따라 변경하여 사용할 수 있습니다.(`src/test/kotlin/MainTest.kt`)  

구현 로직은 `src/main/kotlin/Main.kt`의 `// main logic` 주석 위치에 작성합니다.  
입력 값을 `inputCursor.next()` 로 한 줄씩 가져올 수 있습니다.  

#### 테스트 실행  
로컬에 설치된 gradle을 사용하는 경우,  
`gradle test` 명령어로 테스트를 실행할 수 있습니다.  

설치된 gradle이 없는 경우(wrapper 사용),  
`./gradlew test` 명령어로 테스트를 실행할 수 있습니다.  


