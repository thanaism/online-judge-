fn main(){
    proconio::input!{
        n:usize,q:usize,
        mut a:[i64;n],
        l:[(i64,usize,usize);q]
    }
    let mut shift = 0;
    for k in 0..q {
        let t = l[k].0;
        let i = (l[k].1 - 1 + n - shift)%n;
        let j = (l[k].2 - 1 + n - shift)%n;
        if t==1 { a.swap(i,j) }
        if t==2 { shift += 1 }
        if t==3 { println!("{}",a[i]) }
    }
}