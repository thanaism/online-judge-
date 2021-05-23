main :: IO()
main = do
    [a,b,k] <- map read . words <$> getLine
    putStrLn $ solve k a b

nCk :: Int -> Int -> Int
nCk n k = foldl (\acc (x,y) -> acc * x `div` y) 1 $ zip [n-k+1..n] [1..k]

solve :: Int -> Int -> Int -> String
solve k 0 b = replicate b 'b'
solve k a 0 = replicate a 'a'
solve k a b = if k <= cmb then 'a' : solve k (a-1) b else 'b' : solve (k-cmb) a (b-1)
    where cmb = nCk (a+b-1) (a-1)