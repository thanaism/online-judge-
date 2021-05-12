struct UnionFind { p: Vec<isize> }

impl UnionFind {
    fn new(n:usize) -> UnionFind { UnionFind{ p:vec![-1;n]} }
    fn join(&mut self,x:usize,y:usize) {
        let mut i = self.root(x);
        let mut j = self.root(y);
        if i==j { return }
        if i>j { i=i^j; j=i^j; i=i^j; }
        self.p[i]+=self.p[j];
        self.p[j]=i as isize;
    }

    fn root(&mut self,x:usize) -> usize {
        if self.p[x] < 0 { return x }
        self.p[x] = self.root(self.p[x] as usize) as isize;
        self.p[x] as usize
    }

    fn same(&mut self,x:usize,y:usize) -> bool {
        self.root(x) == self.root(y)
    }
}

struct DisjointSetUnion {
    p: std::collections::HashMap<usize,isize>
}

impl DisjointSetUnion {
    fn new() -> DisjointSetUnion {
        DisjointSetUnion { p: std::collections::HashMap::new() }
    }

    fn root(&mut self, x: usize) -> usize {
        if *self.p.entry(x).or_insert(-1) < 0 { x }
        else {
            let v = self.root(self.p[&x] as usize) as isize;
            self.p.insert(x,v);
            self.p[&x] as usize
        }
    }

    fn join(&mut self,x: usize, y: usize) {
        let mut i = self.root(x);
        let mut j = self.root(y);
        if i==j { return }
        if i>j { i=i^j;j=i^j;i=i^j }
        *self.p.entry(i).or_insert(-1) += *self.p.entry(j).or_insert(-1);
        self.p.insert(j, i as isize);
    }

    fn same(&mut self, x: usize, y: usize) -> bool {
        self.root(x) == self.root(y)
    }
}

fn main() {
    println!("Hello, world!");
    let n = 10;
    let mut uf1 = UnionFind::new(n);
    uf1.join(0,1);
    uf1.join(1,2);
    uf1.join(3,2);
    uf1.join(3,4);
    let mut uf2 = UnionFind::new(n);
    uf2.join(0,1);
    uf2.join(1,2);
    uf2.join(2,3);
    println!("{:?}",uf1.p);
    println!("{}",uf1.same(0,3));
    println!("{}",uf1.same(0,5));
    println!("{:?}",uf2.p);
    println!("{}",uf2.same(0,1));
    println!("{}",uf2.same(0,5));
    let mut dsu = DisjointSetUnion::new();
    dsu.join(0,1);
    dsu.join(2,1);
    dsu.join(4,2);
    dsu.join(3,1);
    println!("{:?}",dsu.p);
    println!("{}",dsu.same(0,4));
}
