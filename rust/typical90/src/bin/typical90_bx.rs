fn main(){
	proconio::input!{
		n:usize,
		a:[usize;n]
	}
	let mut acc = 0;
	let mut que = std::collections::VecDeque::new();
	let total = a.clone().iter().fold(0,|x,i|x+i);
	let mut ok = false;
	for i in 0..2*n {
		que.push_back(a[i%n]);
		acc += a[i%n];
		while acc*10>total {
			let x = que.pop_front().unwrap();
			acc -= x;
		}
		if acc*10==total { ok=true;break }
	}
	println!("{}",if ok {"Yes"} else {"No"});
}
