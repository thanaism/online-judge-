fn main(){
    proconio::input!{
        (n,p,q):(usize,usize,usize),
        a:[usize;n]
    }
    let mut ans = 0;
    for i in 0..n{
        for j in i+1..n{
            for k in j+1..n{
                for l in k+1..n{
                    for m in l+1..n{
                        let s = a[i]%p*a[j]%p*a[k]%p*a[l]%p*a[m]%p;
                        if s==q { ans+=1 }
                    }
                }
            }
        }
    }
    println!("{}",ans);
}