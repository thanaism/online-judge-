fn main() {
    proconio::input!{
        n:usize,
        l:usize
    }
    const MOD:usize = 1_000_000_007;
    let mut dp = vec![0;n+1];
    dp[0] = 1;
    for i in 0..=n {
        if i+l<=n {
            dp[i+l] += dp[i];
            dp[i+l] %= MOD;
        }
        if i+1<=n {
            dp[i+1] += dp[i];
            dp[i+1] %= MOD;
        }
    }
    println!("{}",dp[n]);
}
