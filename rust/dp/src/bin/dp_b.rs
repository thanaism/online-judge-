fn main(){
    proconio::input!{
        n:usize, k:usize, h:[isize;n]
    }
    let mut dp = vec![std::isize::MAX;n];
    dp[0]=0;
    for i in 0..n {
        for j in 1..=k {
            if i>=j {
                dp[i] = dp[i].min(dp[i-j]+(h[i-j]-h[i]).abs());
            }
        }
    }
    println!("{}",dp[n-1]);
}