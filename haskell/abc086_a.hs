main = do
    [a,b] <- map read . words <$> getLine
    let ans = if even (a*b) then "Even" else "Odd"
    putStrLn ans
