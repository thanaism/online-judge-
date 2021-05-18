fn main(){
    proconio::input!{
        n:usize,
        w:usize,
        l:[(usize,usize);n]
    }
    let mut dp = vec![ vec![10isize.pow(11u32);110000]; 110];
    for i in 0..=n { dp[i][0]=0; }
    for i in 1..=n {
        for j in 0..=100000 {
            let c=l[i-1].0;
            let v=l[i-1].1;
            dp[i][j] = dp[i-1][j];
            if j>=v as usize {
                dp[i][j] = dp[i][j].min(
                    dp[i-1][j-v]+c as isize
                );
            }
        }
    }
    for j in (0..=100000).rev() {
        if dp[n][j]<=w as isize {
            println!("{}",j);
            break;
        }
    }
}