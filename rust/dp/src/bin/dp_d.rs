fn main(){
    proconio::input!{
        n:usize, w:usize,
        l:[(usize,usize);n]
    }
    let mut dp = vec![vec![0;w+1];n+1];
    for i in 1..=n {
        for j in 0..=w {
            let v = l[i-1].1;
            let c = l[i-1].0;
            dp[i][j] = dp[i-1][j];
            if j>=c { dp[i][j] = dp[i][j].max(dp[i-1][j-c]+v) }
        }
    }
    println!("{}",dp[n][w]);
}