fn main(){
	proconio::input!{
		(mut n,mut k):(usize,usize)
	}
	const MOD:usize = 100_000;
	
	// kの最大ビット長を求める
	let mut bit_len = 0;
	while k>>bit_len>0 { bit_len+=1 }

	// d[i][j]: 表示jに対して2のi乗回操作を行った結果
	let mut d = vec![vec![0usize;MOD];bit_len];

	// 2の0乗=1回操作を行った際の結果を求める
	for i in 0..MOD {
		let mut x = i;
		let mut s = 0;
		while x>0 {
			s += x%10;
			x /= 10;
		}
		d[0][i] = (i+s)%MOD;
	}

	// 0乗の結果をベースにk乗回操作した結果を算出する
	for i in 1..bit_len {
		for j in 0..MOD {
			let x = d[i-1][j];
			// 結果はMOD通りしかない
			// ゆえに結果を入力にして再度結果を得ることができる
			d[i][j] = d[i-1][x];
		}
	}

	// k回の操作を冪指数ごとに分解（＝ダブリング）して求める
	let mut i = 0;
	while k>0 {
		if k&1==1 { n=d[i][n] }
		k >>= 1;
		i += 1;
	}
	println!("{}",n);
}