import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource
import java.io.File
import java.util.stream.Stream
import kotlin.test.assertEquals

class MainTest {
    companion object {
        private const val TEST_CASE_SEPARATOR = "======" // 테스트 케이스 쌍(입/출력값) 을 구분함.
        private const val DELIMITER = "---" // 하나의 테스트 케이스에서 입력과 출력을 구분함.
        private const val TEST_CASE_SOURCE = "src/test/resources/TestCases.txt" // 테스트 케이스 파일의 위치

        @JvmStatic
        fun testCaseProvider(): Stream<Arguments> {
            val fileContent = File(TEST_CASE_SOURCE).readText().trim()

            val testCases: List<String> = fileContent.split(TEST_CASE_SEPARATOR)

            val parsedTestCases: List<TestCase> = testCases.map { tc ->
                tc.split(DELIMITER).let {
                    TestCase(
                        input = it[0],
                        expected = it[1]
                    )
                }
            }

            return parsedTestCases.map { Arguments.of(it) }.stream()
        }
    }

    @ParameterizedTest
    @MethodSource("testCaseProvider")
    fun resolverTest(testCase: TestCase) {
        val input: List<String> = testCase.input.trim().split("\n")

        val expected: List<String> = testCase.expected.trim().split("\n")

        val output: List<String> = resolver(input)

        assertEquals<String>(
            expected.joinToString(separator = "\n"),
            output.joinToString(separator = "\n")
        )
    }
}
