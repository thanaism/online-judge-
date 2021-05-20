fn main(){
    proconio::input!{ k:usize }
    let mut ans = 0;
    const MOD:usize = 1_000_000_007;
    if k%9==0 {
        let mut dp = vec![0;k+1];
        for i in 1..=9 { dp[i]=1 }
        for i in 1..=k {
            for j in 1..=9 {
                if i>=j { dp[i]+=dp[i-j]; }
            }
            dp[i]%=MOD;
        }
        ans = dp[k];
    }
    println!{"{}",ans};
}