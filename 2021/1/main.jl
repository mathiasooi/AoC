function main()
    s = parse.(Int, readlines("input.txt"))
    println(sum(i -> s[i] > s[i - 1], 2:length(s)))
    println(sum(i -> s[i] > s[i - 3], 4:length(s)))
end

main()
