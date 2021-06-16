use proconio::{input,marker::Chars};
fn main() {
	input!{
		(n, k): (Chars, usize)
	}
	let mut s = Vec::new();
	for c in n.clone().into_iter().rev() {
		s.push(c.to_string().parse::<isize>().unwrap());
	}
	for _ in 0..k {
		let mut ans = 0;
		for (i,d) in s.clone().into_iter().enumerate() {
			let p:isize = 8_isize.pow(i as u32);
			ans += d*p;
		}
		s = Vec::new();
		while ans/9>0 {
			s.push(if ans%9==8 {5} else {ans%9});
			ans /= 9;
		}
		s.push(if ans%9==8 {5} else {ans%9});
	}
	s.iter().rev().for_each(|i|print!("{}",i));
	println!("");
}