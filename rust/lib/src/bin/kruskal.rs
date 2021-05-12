fn main(){
    let mut dsu = DisjointSetUinon{ p:vec![-1;5]};
    println!("{:?}",dsu.p);
    let mut edges = Vec::new();
    let e = Edge{u:3,v:1,cost:25};
    edges.push(e);
    let e = Edge{u:4,v:8,cost:50};
    edges.push(e);
    let e = Edge{u:1,v:2,cost:3};
    edges.push(e);
    let mut kru = Kruskal{dsu:dsu,total:2,edges:edges};
    kru.init();
    println!("{:?}",kru.edges);
}

#[derive(Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge {
    u: usize,
    v: usize,
    cost: isize
}

impl Edge {
}

struct Kruskal {
    dsu: DisjointSetUinon,
    total: isize,
    edges: Vec<Edge>
}

impl Kruskal {
    fn init(&mut self) {
        self.edges.sort_by(|a,b|a.cost.cmp(&b.cost));
    }
}

struct DisjointSetUinon {
    p: Vec<isize>
}

impl DisjointSetUinon {
    fn join(&mut self,x:usize,y:usize){
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
        if self.root(x) == self.root(y) { true }
        else { false }
    }
}