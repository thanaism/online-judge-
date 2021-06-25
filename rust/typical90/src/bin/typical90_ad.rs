fn main(){
	proconio::input!{
		(n,k):(usize,usize)
	}
	let mut cnt=vec![0;n+1];
	for i in 2..=n {
		if cnt[i]>0 {continue}
		let mut j = i;
		while j<=n {
			cnt[j]+=1;
			j+=i;
		}
	}
	let mut ans=0;
	for i in 0..=n {
		if cnt[i]>=k {ans+=1}
	}
	println!("{}",ans);
}