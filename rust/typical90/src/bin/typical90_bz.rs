fn main() {
	proconio::input!{
		(n,m):(usize,usize),
		ls:[(usize,usize);m]
	}
	let mut edges = vec![0;n];
	for i in 0..m {
		let (a,b) = ls[i];
		if a<b {
			edges[b-1] += 1;
		} else {
			edges[a-1] += 1;
		}
	}
	let mut ans = 0;
	for i in 0..n {
		if edges[i]==1 {
			ans += 1;
		}
	}
	println!("{}",ans);
}