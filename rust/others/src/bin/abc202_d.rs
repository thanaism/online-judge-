fn main(){
    proconio::input!{
        (a,b,k):(usize,usize,usize)
    }
    println!("{}",solve(a,b,k))
}

fn cmb(n:usize,k:usize) -> usize {
    (n-k+1..=n).zip(1..=k).fold(1,|acc,(x,y)|acc*x/y)
}

fn solve(a:usize,b:usize,k:usize) -> String {
    let c=cmb(a+b-1,a-1);
    match (a,b,k) {
        (0,_,_) => "b".to_string().repeat(b),
        (_,0,_) => "a".to_string().repeat(a),
        (_,_,_) if k<=c => format!("{}{}","a",solve(a-1,b,k)),
        (_,_,_) => format!("{}{}","b",solve(a,b-1,k-c))
    }
}