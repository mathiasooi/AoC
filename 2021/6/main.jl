using DataStructures

function solve(n)
    fish = counter(parse.(Int, split(read("input.txt", String), ',')))
    
    for _ in 1:n
        x = fish[0]
        for i in 1:9
            fish[i-1] = fish[i]
        end
        fish[6] += x
        fish[8] = x
    end
    println(sum(fish))
end
solve(80)
solve(256)