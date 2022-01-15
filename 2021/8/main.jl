function p1()
    outputs = [split(s, " | ")[2] for s in readlines("input.txt")]
    total = 0
    for output in outputs
        for i in split(output)
            total += in(length(i), [2, 3, 4, 7])
        end
    end
    println(total)
end
p1()
