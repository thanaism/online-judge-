fn main() {
    proconio::input!{
        (n,k,p):(usize,usize,usize),
        a:[usize;n]
    }
    let n1 = n/2;
	let mut a1 = vec![Vec::new();100];
	for i in 0..1<<n1 {
		let mut c = 0;
		let mut v = 0;
		for j in 0..n1 {
			if i>>j&1==1 {
				v += a[j];
				c += 1;
			}
		}
		a1[c].push(v);
	}
	
	let n2 = n-n1;
	let mut a2 = vec![Vec::new();100];
	for i in 0..1<<n2 {
		let mut c = 0;
		let mut v = 0;
		for j in 0..n2 {
			if i>>j&1==1 {
				v += a[j+n1];
				c += 1;
			}
		}
		a2[c].push(v);
	}
	for i in 0..n {
		a1[i].sort_unstable();
		a2[i].sort_unstable();
	}

	let mut ans = 0;
	for i in 0..=k {
		if a1[i].len()==0 { continue }
		for j in 0..a1[i].len() {
			if k<i { continue }
			if a2[k-i].len()==0 { continue }
			if a1[i][j]+a2[k-i][0]>p { continue }
			if a1[i][j]+a2[k-i][a2[k-i].len()-1]<=p {
				ans+=a2[k-i].len() as isize;
				continue;
			}
			let mut ng = 0isize;
			let mut ok = (a2[k-i].len()-1) as isize;
			while (ng-ok).abs()>1 {
				let mid = ((ok+ng)/2) as usize;
				if a1[i][j]+a2[k-i][mid]>p { ok = mid as isize }
				else { ng = mid as isize}
			}
			ans += ok;
		}
	}
	println!("{}",ans);
}