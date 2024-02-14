# Makefile

# 컴파일러 설정
CC = g++

# 컴파일 플래그 설정
CFLAGS = -std=c++17

SOURCE = main.cpp
EXECUTABLE = main

# 기본 타겟 설정
all: compile_and_test

# 실행 파일 컴파일
$(EXECUTABLE): $(SOURCE)
	$(CC) $(CFLAGS) -o $@ $^

# 파이썬 테스트 실행
test:
	python test.py

# Makefile 정리 타겟
clean:
	rm -f $(EXECUTABLE)

compile_and_test:
	$(MAKE) $(EXECUTABLE)
	-$(MAKE) test
	$(MAKE) clean
