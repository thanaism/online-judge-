use proconio::{input,marker::Chars};
fn main(){
    input!{
        (n,k):(usize,usize),
        s:Chars
    }
    let mut c = vec![vec![n;26];n+1];
    for i in (0..n).rev() {
        for j in 0..26 {
            if s[i] as usize - 'a' as usize==j {
                c[i][j] = i;
            } else {
                c[i][j] = c[i+1][j];
            }
        }
    }
    let mut ans = String::new();
    let mut x = 0;
    for i in 0..k {
        for j in 0..26 {
            let y = c[x][j];
            let l = n-y+i;
            if l>=k {
                let ch = (97 + j) as u8 as char;
                ans.push(ch);
                x = y+1;
                break;
            }
        }
    }
    println!("{}",ans);
}