use proconio::input;
fn main() {
	input!{n:usize}
	let mut x = n;
	let mut cnt = 0;
	for i in 2..n {
		if i*i>n {break}
		while x%i==0 {
			x /= i;
			cnt += 1;
		}
	}
	if x!=1 {cnt+=1}
	let mut ans = 0;
	let mut i = 1;
	while i<cnt {
		ans += 1;
		i *= 2;
	}
	println!("{}",ans);
}
