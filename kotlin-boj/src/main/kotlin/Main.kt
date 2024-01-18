class Main

fun main() {
    val input: List<String> = generateSequence(::readlnOrNull).toList()
    val output: List<String> = resolver(input)
    output.forEach(::println)
}

fun resolver(input: List<String>): List<String> {
    val inputCursor = input.iterator()
    val output: MutableList<String> = mutableListOf()

    // main logic

    return output
}

