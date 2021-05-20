fn main(){
    proconio::input!{
        a:i128,
        b:i128
    }
    let ans = lcm(a,b);
    if ans>10i128.pow(18u32) {
        println!{"{}","Large"}
    } else {
        println!("{}",ans)
    }
}

fn lcm(x:i128,y:i128)->i128{
    x*y/gcd(x,y)    
}

fn gcd(x:i128,y:i128)->i128{
    if y==0 {return x}
    gcd(y,x%y)
}