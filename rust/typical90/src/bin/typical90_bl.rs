use proconio::{input,marker::Usize1};
fn main(){
	input!{
		(n,q):(usize,usize),
		a:[isize;n],
		ls:[(Usize1,Usize1,isize);q]
	}
	let mut d:Vec<isize> = (1..n).map(|i|a[i]-a[i-1]).collect();
	let mut t:isize = (1..n).fold(0,|acc,x|acc+(a[x]-a[x-1]).abs());
	for i in 0..q {
		let (l,r,v) = ls[i];
		if l>0 {
			let d1 = d[l-1].abs();
			d[l-1] += v;
			t += d[l-1].abs()-d1;
		}
		if r+1<n {
			let d1 = d[r].abs();
			d[r] -= v;
			t += d[r].abs()-d1;
		}
		println!("{}",t);
	}
}