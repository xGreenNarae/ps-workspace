class Main

fun main() {
    // fast I/O
    val reader = System.`in`.bufferedReader()
    val writer = System.out.bufferedWriter()

    val input: List<String> = generateSequence { reader.readLine() }.toList()
    val output: List<String> = resolver(input)
    output.forEach { writer.write("$it\n") }

    writer.flush()
    reader.close()
    writer.close()
}

fun resolver(input: List<String>): List<String> {
    val inputCursor = input.iterator()
    val output: MutableList<String> = mutableListOf()

    // main logic

    return output
}
