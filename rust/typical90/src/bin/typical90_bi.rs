use std::collections::VecDeque;
fn main(){
	proconio::input!{
		q:usize,
		l:[(usize,usize);q]
	}
	let mut dq = VecDeque::new();
	for i in 0..q {
		if l[i].0==3 {
			let x = l[i].1-1;
			println!("{}",dq[x]);
		}
		if l[i].0==1 {
			let x = l[i].1;
			dq.push_front(x);
		}
		if l[i].0==2 {
			let x = l[i].1;
			dq.push_back(x);
		}
	}
}
