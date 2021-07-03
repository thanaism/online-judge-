use proconio::{input,marker::Chars};
use itertools::iproduct;

fn u(i:isize) -> usize { i as usize }

fn main() {
	input!{
		(h,w):(isize,isize),
		g:[Chars;h]	
	}
	let mut dfs = GridGraph::new(h, w, g);
	let mut ans = -1;
	for (i,j) in iproduct!(0..h,0..w) {
		let ret = dfs.rec(i,j,i,j);
        ans = ans.max(ret);
	}
	if ans<3 { ans = -1; }
	println!("{}",ans);
}

struct GridGraph {
	g: Vec<Vec<char>>,
	h: isize,
	w: isize,
	used: Vec<Vec<bool>>
}

impl GridGraph {
	fn new(h:isize,w:isize,g:Vec<Vec<char>>) -> Self {
		GridGraph {
			g: g,
			h: h,
			w: w,
			used: vec![vec![false;u(w)];u(h)]
		}
	}
	fn rec(&mut self, si:isize, sj:isize, ci:isize, cj:isize) -> isize {
		let di = [0,1,0,-1];
		let dj = [-1,0,1,0];
		if ci==si && cj==sj && self.used[u(ci)][u(cj)] { return 0 }
		self.used[u(ci)][u(cj)]=true;
		let mut dist = -(1<<60);
		for i in 0..4 {
			let ni = ci + di[i];
			let nj = cj + dj[i];
            if ni<0 || ni>=self.h || nj<0 || nj>=self.w { continue }
			if self.g[u(ni)][u(nj)]=='#' { continue } 
			if (ni!=si || nj!=sj) && self.used[u(ni)][u(nj)] { continue }
            let v = self.rec(si,sj,ni,nj);
            dist = dist.max(v+1);
		}
		self.used[u(ci)][u(cj)] = false;
		dist
	}
}