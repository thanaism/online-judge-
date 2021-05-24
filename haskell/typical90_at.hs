import Data.List ( sort, group )
main = do
    n <- readLn
    a <- map read . words <$> getLine
    b <- map read . words <$> getLine
    c <- map read . words <$> getLine
    print $ solve n a b c

solve :: Int -> [Int] -> [Int] -> [Int] -> [[Int]]
solve n a b c = m a
    where ls = [(i,j,k)|i<-[0..45],j<-[0..45],k<-[0..45],mod(i+j+k)46==0]

m :: [Int] -> [[Int]]
m l = group $ sort $ map (`mod`46) l