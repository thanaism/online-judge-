fn main(){
	proconio::input!{
		(n,k):(usize,i128)
	}
	let l = (k-1).max(0);
	let mut m = (k-2).max(0);
	const MOD:i128 = 1000_000_007;
	let mut ans = 1;
	if n<2 {
		for i in 0..n {
			if i==0 { ans = k }
			else if i==1 { ans *= l }
			else { ans *= m }
			ans %= MOD;
		}
	} else {
		let mut x = n-2;
		while x>0 {
			if x&1==1 { ans = ans * m % MOD }
			m = m * m % MOD;
			x >>= 1;
		}
		ans = ans * k % MOD * l % MOD;
	}
	println!("{}",ans);
}