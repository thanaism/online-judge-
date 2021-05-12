fn main() {
    println!("Hello, world!");
    let n = 10;
    let mut dsu1 = DisjointSetUnion{ p: vec![-1;n]};
    dsu1.join(0,1);
    dsu1.join(1,2);
    dsu1.join(3,2);
    dsu1.join(3,4);
    let mut dsu2 = DisjointSetUnion{ p: vec![-1;n]};
    dsu2.join(0,1);
    dsu2.join(1,2);
    dsu2.join(2,3);
    println!("{:?}",dsu1.p);
    println!("{}",dsu1.same(0,3));
    println!("{}",dsu1.same(0,5));
    println!("{:?}",dsu2.p);
    println!("{}",dsu2.same(0,5));
}

struct DisjointSetUnion {
    p: Vec<isize>
}

impl DisjointSetUnion {
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