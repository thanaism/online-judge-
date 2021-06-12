fn main(){
	proconio::input!{
		(h,w):(usize,usize),
		p:[[usize;w];h]
	}
	let mut ans = 0;
	for b in 0..1<<h {
		let mut d = std::collections::HashMap::new();
		for j in 0..w {
			let mut x = 0;
			let mut cnt = 0;
			let mut ok = true;
			for i in 0..h {
				if b>>i&1==1 {
					if x==0 {x=p[i][j]}
					if p[i][j]!=x {
						ok=false;
						break
					}
					cnt += 1;
				}
			}
			if ok {*d.entry(x).or_insert(0)+=cnt}
		}
		for (_,v) in d {
			ans=ans.max(v);
		}
	}
	println!("{}",ans);
}