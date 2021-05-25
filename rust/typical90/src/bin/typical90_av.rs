fn main() {
    proconio::input!{
        (n,k):(usize,usize),
        mut l:[(usize,usize);n]
    }
    let mut q:Vec<usize> = l.into_iter()
        .map(|x|vec![x.0-x.1,x.1])
        .flatten()
        .collect();
    q.sort();
    let ans:usize = q.into_iter().rev().take(k).sum();
    println!("{}",ans);
}