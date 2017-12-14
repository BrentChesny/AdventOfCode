import Control.Monad (liftM)
import Data.Char (digitToInt)
import Data.String.Utils (strip)
import Text.Printf (printf)

solvePartOne :: String -> Int
solvePartOne puzzle = sumOfEqualValues digits (rotate 1 digits)
  where
    digits = map digitToInt puzzle

solvePartTwo :: String -> Int
solvePartTwo puzzle = sumOfEqualValues digits (rotate (div (length digits) 2) digits)
  where
    digits = map digitToInt puzzle

rotate :: Int -> [a] -> [a]
rotate n xs = take (length xs) (drop n (cycle xs))

sumOfEqualValues :: [Int] -> [Int] -> Int
sumOfEqualValues (x:xs) (y:ys) = if x == y
  then x + (sumOfEqualValues xs ys)
  else sumOfEqualValues xs ys
sumOfEqualValues [] [] = 0

main :: IO ()
main = do
    input <- liftM strip (readFile "input.txt")
    printf "Part one: %d\n" (solvePartOne input)
    printf "Part two: %d\n" (solvePartTwo input)
