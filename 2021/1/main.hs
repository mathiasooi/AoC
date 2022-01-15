main :: IO ()
main = do
    contents <- readFile "input.txt"
    let xs = map (read :: String -> Int) . words $ contents
    print $ part1 $ xs
    print $ part2 $ xs
    
part1 :: [Int] -> Int
part1 xs = sum $ map (\x -> if ((xs !! x) > (xs !! (x-1))) then 1 else 0 ) [1..(length xs)-1]

part2:: [Int] -> Int
part2 xs = sum $ map (\x -> if ((xs !! x) > (xs !! (x-3))) then 1 else 0 ) [3..(length xs)-1]