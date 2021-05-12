struct Edge {
    u: usize,
    v: usize,
    cost: isize,
}

struct Kruskal {
    uf: UnionFind,
    total: isize,
    edges: Vec<Edge>,
}

impl Kruskal {
    fn init(vec: Vec<Edge>, vmax: usize) -> isize {
        let mut krs = Kruskal {
            uf: UnionFind::new(vmax),
            total: 0,
            edges: vec,
        };
        krs.edges.sort_by(|a, b| a.cost.cmp(&b.cost));
        for e in krs.edges {
            if !krs.uf.same(e.u, e.v) {
                krs.uf.join(e.u, e.v);
                krs.total += e.cost;
            }
        }
        krs.total
    }
}

struct UnionFind { p: Vec<isize>, }

impl UnionFind {
    fn new(n: usize) -> UnionFind {
        UnionFind { p: vec![-1; n] }
    }
    fn join(&mut self, x: usize, y: usize) {
        let mut i = self.root(x);
        let mut j = self.root(y);
        if i == j { return; }
        if i > j { i=i^j; j=i^j; i=i^j; }
        self.p[i] += self.p[j];
        self.p[j] = i as isize;
    }

    fn root(&mut self, x: usize) -> usize {
        if self.p[x] < 0 { return x }
        self.p[x] = self.root(self.p[x] as usize) as isize;
        self.p[x] as usize
    }

    fn same(&mut self, x: usize, y: usize) -> bool {
        self.root(x) == self.root(y)
    }
}

fn main() {
    // AOJ - Minimum Spanning Tree
    // https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=ja
    let mut edges = Vec::new();
    let mut ps = |x, y, z| {
        edges.push(Edge { u: x, v: y, cost: z })
    };
    ps(0, 1, 1);
    ps(0, 2, 3);
    ps(1, 2, 1);
    ps(1, 3, 7);
    ps(2, 4, 1);
    ps(1, 4, 3);
    ps(3, 4, 1);
    ps(3, 5, 1);
    ps(4, 5, 6);
    let krs = Kruskal::init(edges, 10001);
    println!("{}", krs);
}
