fn main() {
	proconio::input!{
		n: usize,
		ls: [(usize,usize);n]
	}
	let mut ans:f64 = 0.0;
	for i in 0..n {
		for j in i+1..n {
			let (l0, r0) = ls[i];
			let (l1, r1) = ls[j];
			let mut numer = 0;
			let mut denom = 0;
			for k in l0..=r0 {
				for l in l1..=r1 {
					if k>l { numer += 1 }
					denom += 1;
				}
			}
			ans += numer as f64 / denom as f64;
		}
	}
	println!("{}",ans);
}