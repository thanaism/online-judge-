fn main(){
	proconio::input!{
		(l,r):(i128,i128)
	}
	let nl =l.to_string().len() as i128;
	let nr =r.to_string().len() as i128;
	const MOD:i128 = 1000_000_007;
	let mut ans = 0;
	let mut left = l;
	for i in nl..=nr {
		let d = 10i128.pow(i as u32)-1;
		let right = r.min(d);
		let n = right-left+1;
		let mut t = left+right;
		t *= n; t /= 2; t %= MOD;
		t *= i; t %= MOD;
		ans += t; ans %= MOD;
		left = right+1;
	}
    println!("{}",ans);
}