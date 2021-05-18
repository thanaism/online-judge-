fn main(){
    proconio::input!{ n:usize, h:[isize;n] }
    let mut dp = vec![0;n];
    dp[1] = dp[0]+(h[1]-h[0]).abs();
    for i in 2..n {
        dp[i] = std::cmp::min(dp[i-1]+(h[i-1]-h[i]).abs(),dp[i-2]+(h[i-2]-h[i]).abs());
    }
    println!("{}",dp[n-1]);
}