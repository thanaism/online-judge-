fn main() {
	proconio::input!{
		n: usize,
		l: [(isize, isize);n]
	}
	let mut xs = Vec::new();
	let mut ys = Vec::new();
	for (x,y) in l {
		xs.push(x);
		ys.push(y);
	}
	xs.sort();
	ys.sort();
	let mid_x;
	let mid_y;
	if n&1==1 {
		mid_x = xs[n/2]*2;
		mid_y = ys[n/2]*2;
	} else {
		let m = n/2;
		mid_x = xs[m]+xs[m-1];
		mid_y = ys[m]+ys[m-1];
	}
	let mut ans = 0;
	for i in 0..n {
		ans += (xs[i]*2-mid_x).abs();
		ans += (ys[i]*2-mid_y).abs();
	}
	println!("{}",ans/2);
}