use proconio::{input,marker::Chars};
fn main(){
    input!{
        s:Chars,
        t:Chars
    }
    let mut dp = vec![vec![0;t.len()+1];s.len()+1];
    for i in 1..=s.len() {
        for j in 1..=t.len() {
            dp[i][j] = dp[i-1][j].max(dp[i][j-1]);
            if s[i-1]==t[j-1] {
                dp[i][j]=dp[i][j].max(dp[i-1][j-1]+1);
            }
        }
    }
    let mut ans = String::new();
    let mut i = s.len();
    let mut j = t.len();
    while i>0 && j>0 {
        if dp[i][j] == dp [i-1][j] {i-=1}
        else if dp[i][j] == dp [i][j-1] {j-=1}
        else {
            ans.push(s[i-1]);
            i-=1;
            j-=1;
        }
    }
    println!("{}",ans);
}