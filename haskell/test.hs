chain::Integer->[Integer]
chain 1=[1]
chain n
    |even n=n:chain (div n 2)
    |odd n=n:chain (n*3+1)

map'::(a->b)->[a]->[b]
map' _ []=[]
map' f (x:y)=f x:map' f y

fact :: Int -> Int
fact 0 = 1
fact n = n * fact ( n - 1 )

firstLetter :: String -> String
firstLetter "" = "DO NOT ENTER EMPTY STRING!"
firstLetter all@(x:xs) = [x] ++ ": " ++ all

isYoung :: Int -> String
isYoung age
    | age < 20 = "You're young!"
    | age > 70 = "You're almost dead!"
    | otherwise = "You're old!"

isPriceLow :: Int -> String
isPriceLow price
    | taxed < 220*100 = "price is low."
    | taxed > 550*100 = "price is high."
    | otherwise = "price is not low."
    where taxed = price * 110
