using DataStructures

function p1()
    d = DataStructures.DefaultDict{Int, Int}(0)
    len = 12
    for line in readlines("input.txt")
        for i in 1:len
            d[i] += line[i] == '1' ? 1 : -1
        end
    end
    gamma, epsilon = 0, 0
    for i in 1:len
        if d[i] > 0
            gamma += 2 ^ (len - i)
        else
            epsilon += 2 ^ (len - i)
        end
    end
    println(gamma * epsilon)
end

function p2()
    s1 = Set{String}(readlines("input.txt"))
    s2 = Set{String}(readlines("input.txt"))
    i = 1
    while length(s1) != 1
        new = Set{String}()
        if sum(x -> x[i] == '1', s1) >= length(s1) / 2
            for s in s1
                if s[i] == '1'
                    push!(new, s)
                end
            end
        else
            for s in s1
                if s[i] == '0'
                    push!(new, s)
                end
            end
        end
        i += 1
        empty!(s1)
        union!(s1, new)
    end
    i = 1
    while length(s2) != 1
        new = Set{String}()
        if sum(x -> x[i] == '1', s2) < length(s2) / 2
            for s in s2
                if s[i] == '1'
                    push!(new, s)
                end
            end
        else
            for s in s2
                if s[i] == '0'
                    push!(new, s)
                end
            end
        end
        i += 1
        empty!(s2)
        union!(s2, new)
    end
    println(parse(Int, pop!(s1); base=2) * parse(Int, pop!(s2); base=2))
end

p1()
p2()
