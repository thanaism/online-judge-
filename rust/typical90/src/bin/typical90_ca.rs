fn main() {
	proconio::input!{
		(h,w):(usize,usize),
		mut a:[[isize;w];h],
		b:[[isize;w];h]
	}
	let mut cnt = 0;
	for i in 0..h-1 {
		for j in 0..w-1 {
			let diff = b[i][j] - a[i][j];
			if diff!=0 { cnt+=diff.abs() }
			for k in 0..2 {
				for l in 0..2 {
					a[i+k][j+l] += diff;
				}
			}
		}
	}
	let mut ans = true;
	for i in 0..h {
		for j in 0..w {
			if a[i][j]!=b[i][j] {
				ans = false;
			}
		}
	}
	if ans {
		println!("{}","Yes");
		println!("{}",cnt);
	} else {
		println!("{}","No");
	}
}