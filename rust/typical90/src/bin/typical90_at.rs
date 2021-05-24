use itertools::iproduct;
fn main() {
    proconio::input!{
        n:usize,
        a:[usize;n],
        b:[usize;n],
        c:[usize;n]
    }
    let m = |x:Vec<usize>|x.into_iter()
    .fold(vec![0i128;46],|mut v,x|{v[x%46]+=1;v});
    let ma = m(a);
    let mb = m(b);
    let mc = m(c);
    let ans:i128 = iproduct!(0..46,0..46,0..46)
        .filter(|(i,j,k)|(i+j+k)%46==0)
        .fold(0,|acc,(i,j,k)|acc+ma[i]*mb[j]*mc[k]);
    println!("{}",ans);
}