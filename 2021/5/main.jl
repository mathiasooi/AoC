using DataStructures

function p1()
    d = DataStructures.DefaultDict{Pair{Int, Int}, Int}(0)
    for line in readlines("input.txt")
        s, e = [parse.(Int, split(i, ',')) for i in split(line, " -> ")]
        if s[1] == e[1]  # Vertical line
            for i in min(s[2], e[2]):max(s[2], e[2])
                d[Pair(s[1], i)] += 1
            end
        elseif s[2] == e[2]  # Horizontal line
            for i in min(s[1], e[1]):max(s[1], e[1])
                d[Pair(i, s[2])] += 1
            end
        end
    end
    println(sum((item -> item.second >= 2), d))
end

function p2()
    d = DataStructures.DefaultDict{Pair{Int, Int}, Int}(0)
    for line in readlines("input.txt")
        s, e = [parse.(Int, split(i, ',')) for i in split(line, " -> ")]
        if s[1] == e[1]  # Vertical line
            for i in min(s[2], e[2]):max(s[2], e[2])
                d[Pair(s[1], i)] += 1
            end
        elseif s[2] == e[2]  # Horizontal line
            for i in min(s[1], e[1]):max(s[1], e[1])
                d[Pair(i, s[2])] += 1
            end
        elseif abs(s[1] - e[1]) == abs(s[2] - e[2])
            dx = s[1] > e[1] ? -1 : 1
            dy = s[2] > e[2] ? -1 : 1
            cx, cy = s
            while cx != e[1]
                d[Pair(cx, cy)] += 1
                cx += dx
                cy += dy
            end
            d[Pair(cx, cy)] += 1
        end
    end
    println(sum((item -> item.second >= 2), d))
end
p1()
p2()
