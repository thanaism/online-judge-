import Data.Bits (shiftR)

main :: IO ()
main = do
    getLine
    a <- map read . words <$> getLine
    print $ solve a

solve :: [Int] -> Int
solve a = minimum $ map div2 a

div2 :: Int -> Int
div2 x
    | even x = 1 + div2 (shiftR x 1)
    | otherwise = 0