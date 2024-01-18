use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let input: Vec<&str> = input.trim().split('\n').collect();
    let output = resolver(&input);
    for line in output {
        println!("{}", line);
    }
}

fn resolver(input: &[&str]) -> Vec<String> {
    let mut input_cursor = input.iter();
    let mut output = Vec::new();

    // main logic


    output
}


#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;

    const TEST_CASE_SEPARATOR: &str = "======";
    const DELIMITER: &str = "---";
    const TEST_CASE_SOURCE: &str = "test/TestCases.txt";

    #[test]
    fn resolver_test() {
        let test_cases = fs::read_to_string(TEST_CASE_SOURCE).unwrap();
        let test_cases: Vec<&str> = test_cases.split(TEST_CASE_SEPARATOR).collect();

        for case in test_cases {
            let parts: Vec<&str> = case.split(DELIMITER).collect();
            let input = parts[0].trim().split('\n').collect::<Vec<&str>>();
            let expected = parts[1].trim().split('\n').collect::<Vec<&str>>();

            let output = resolver(&input);
            assert_eq!(output, expected);
        }
    }
}
