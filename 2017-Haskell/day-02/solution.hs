import Text.Printf (printf)
import Data.List.Split (splitOn)

solvePartOne :: [[Int]] -> Int
solvePartOne puzzle = sum (map diffBetweenMinAndMax puzzle)

diffBetweenMinAndMax :: [Int] -> Int
diffBetweenMinAndMax nums = (maximum nums) - (minimum nums)

solvePartTwo :: [[Int]] -> Int
solvePartTwo puzzle = sum (map findProperDivisors puzzle)

findProperDivisors :: [Int] -> Int
findProperDivisors [] = 0
findProperDivisors (x:xs) = if (doesDivideAny x xs) /= 0
  then doesDivideAny x xs
  else findProperDivisors xs

doesDivideAny :: Int -> [Int] -> Int
doesDivideAny n (x:xs) = if mod n x == 0
  then div n x
  else if mod x n == 0
    then div x n
    else doesDivideAny n xs
doesDivideAny n [] = 0

parseMatrix :: String -> [[Int]]
parseMatrix input = map func (lines input)
  where
    func s = map (read::String->Int) (splitOn "\t" s)

main :: IO ()
main = do
  input <- readFile "input.txt"
  printf "Part one: %d\n" (solvePartOne (parseMatrix input))
  printf "Part two: %d\n" (solvePartTwo (parseMatrix input))
