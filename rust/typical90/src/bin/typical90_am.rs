use proconio::input;
fn main(){
	input!{
		n:usize
	}
	let mut edges = vec![Vec::new();1<<18];
	let mut la = Vec::new();
	let mut lb = Vec::new();
	for _ in 0..n-1 {
		input!{
			(a,b):(usize,usize)
		}
		la.push(a);
		lb.push(b);
		edges[a].push(b);
		edges[b].push(a);
	}
	let mut ans = 0;
	let mut dfs = DFS::new(edges);
	dfs.dfs(1,-1);
	for i in 0..n-1 {
		let a = dfs.dp[la[i]];
		let b = dfs.dp[lb[i]];
		let r = if a<b {a} else {b};
		ans += r * (n-r);
	}
	println!("{}",ans);
}

struct DFS {
	edges: Vec<Vec<usize>>,
	dp: Vec<usize>
}

impl DFS {
	fn new(edges:Vec<Vec<usize>>) -> Self {
		DFS {
			edges: edges,
			dp: vec![0;1<<18]
		}
	}
	fn dfs(&mut self, pos:usize, pre:isize) {
		self.dp[pos] = 1usize;
		for i in self.edges[pos].clone() {
			if i as isize==pre {continue}
			self.dfs(i, pos as isize);
			self.dp[pos] += self.dp[i];
		}
	}
}