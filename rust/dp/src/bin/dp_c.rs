fn main(){
    proconio::input!{
        n:usize,
        l:[(isize,isize,isize);n]
    }
    let mut dp_a = vec![0;n];
    let mut dp_b = vec![0;n];
    let mut dp_c = vec![0;n];
    dp_a[0]=l[0].0;
    dp_b[0]=l[0].1;
    dp_c[0]=l[0].2;
    for i in 1..n {
        dp_a[i] = *[
            dp_b[i-1]+l[i].0,
            dp_c[i-1]+l[i].0
        ].iter().max().unwrap();
        dp_b[i] = *[
            dp_c[i-1]+l[i].1,
            dp_a[i-1]+l[i].1
        ].iter().max().unwrap();
        dp_c[i] = *[
            dp_a[i-1]+l[i].2,
            dp_b[i-1]+l[i].2
        ].iter().max().unwrap();
    }
    let ans = *[
        dp_a[n-1],
        dp_b[n-1],
        dp_c[n-1]
    ].iter().max().unwrap();
    println!("{}",ans);
}