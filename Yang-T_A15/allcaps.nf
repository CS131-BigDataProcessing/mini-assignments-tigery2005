
params.str = "Hello World"

process toUpperCase {
    input:
    val str
    
    output:
    file 'result.txt'

    script:
    """
    echo '${str.toUpperCase()}' > result.txt
    """
}

workflow {
    def channel = Channel.from(params.str)
    def result = toUpperCase(channel)
    result.view { file -> file.text }
}

