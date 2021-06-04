use proconio::{input,marker::Usize1};

struct SCC {
    n: usize,
    e_obv: Vec<Vec<usize>>,
    e_inv: Vec<Vec<usize>>,
    seen: Vec<bool>,
    order: Vec<usize>,
    cnt: i128,
}

impl SCC {
    pub fn new(nodes:usize, e_obv:Vec<Vec<usize>>, e_inv:Vec<Vec<usize>>) -> Self {
        SCC {
            n:nodes,
            e_obv:e_obv,
            e_inv:e_inv,
            seen:vec![false;nodes],
            order:Vec::new(),
            cnt:0,
        }
    }
    fn dfs1(&mut self, i:usize) {
        self.seen[i] = true;
        for e in self.e_obv[i].clone().into_iter() {
            if !self.seen[e] {
                self.dfs1(e);
            }
        }
        self.order.push(i);
    }
    fn dfs2(&mut self, i:usize) {
        self.seen[i] = true;
        self.cnt+=1;
        for e in self.e_inv[i].clone().into_iter() {
            if !self.seen[e] {
                self.dfs2(e);
            }
        }
    }
    pub fn solve(&mut self) -> i128 {
        for i in 0..self.n {
            if !self.seen[i] {
                self.dfs1(i);
            }
        }
        let mut ans = 0i128;
        for i in 0..self.n { self.seen[i] = false }
        for i in self.order.clone().into_iter().rev() {
            if self.seen[i] { continue }
            self.cnt = 0i128;
            self.dfs2(i);
            ans += self.cnt * (self.cnt-1) / 2;
        }
        ans
    }
}

fn main(){
    let stack_size = 104_857_600;
    let thd = std::thread::Builder::new().stack_size(stack_size);
    thd.spawn(|| solve()).unwrap().join().unwrap();
}

fn solve(){
    input!{
        (n,m):(usize,usize),
        l:[(Usize1,Usize1);m]
    }
    let (e_obv,e_inv) = l
    .into_iter()
    .fold(
        (vec![Vec::new();n],vec![Vec::new();n]),
        |(mut v1,mut v2),(a,b)|{v1[a].push(b);v2[b].push(a);(v1,v2)}
    );
    let mut scc = SCC::new(n, e_obv, e_inv);
    let ans = scc.solve();
    println!("{}",ans);        
}