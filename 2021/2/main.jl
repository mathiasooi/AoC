function p1()
    h, v = 0, 0
    for line in readlines("input.txt")
        op, x = split(line)
        x = parse(Int, x)
        if op == "forward"
            h += x
        elseif op == "up"
            v -= x
        else
            v += x
        end
    end
    println(h * v)
end

function p2()
    h, v, a = 0, 0, 0
    for line in readlines("input.txt")
        op, x = split(line)
        x = parse(Int, x)
        if op == "down"
            a += x
        elseif op == "up"
            a -= x
        else
            h += x
            v += x * a
        end
    end
    println(h * v)
end

p1()
p2()
