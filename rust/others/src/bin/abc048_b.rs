fn main() {
    proconio::input! {a:i64,b:i64,x:i64}
    println!("{}", b / x - a / x + if a % x == 0 { 1 } else { 0 })
}
