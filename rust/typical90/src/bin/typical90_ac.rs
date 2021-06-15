struct LazySegmentTree {
    size: usize,
    nodes: Vec<isize>,
    lazy: Vec<isize>,
    id: isize,
    fn_get: fn(a:isize,b:isize)->isize,
    fn_update: fn(a:isize,b:isize)->isize
}

#[allow(dead_code)]
impl LazySegmentTree {
    fn new(n:usize,v:Vec<isize>,id:isize,fn_get:fn(a:isize,b:isize)->isize,fn_update:fn(a:isize,b:isize)->isize) -> Self {
        let size = n.next_power_of_two();
        let mut nodes = vec![id;2*size-1];
        let lazy = vec![id;2*size-1];
        for i in 0..n { nodes[i+size-1]=v[i] }
        for i in (0..size-1).rev() {
            nodes[i] = fn_get(nodes[2*i+1],nodes[2*i+2])
        }
        LazySegmentTree {
            size: size,
            nodes: nodes,
            lazy: lazy,
            id: id,
            fn_get: fn_get,
            fn_update: fn_update
        }
    }
    fn eval(&mut self,k:usize,l:usize,r:usize) {
        if self.lazy[k]!=self.id {
            self.nodes[k] = (self.fn_get)(self.nodes[k],self.lazy[k]);
            if r-l>1 {
				self.lazy[2*k+1] = (self.fn_get)(self.lazy[2*k+1],self.lazy[k]);
				self.lazy[2*k+2] = (self.fn_get)(self.lazy[2*k+2],self.lazy[k]);
            }
            self.lazy[k] = self.id;
        }
    }
    fn get(&mut self, l:usize, r:usize) -> isize {
        let ret = self._get(l,r,0,self.size,0);
        ret
    }
    fn _get(&mut self,ql:usize,qr:usize,l:usize,r:usize,i:usize) -> isize {
        if qr<=l || r<=ql {
            self.id
        } else if ql<=l && r<=qr {
            self.eval(i, l, r);
            self.nodes[i]
        } else {
            self.eval(i, l, r);
            let a = self._get(ql,qr,l,(l+r)/2,2*i+1);
            let b = self._get(ql,qr,(l+r)/2,r,2*i+2);
            (self.fn_get)(a,b)
        }
    }
    fn update(&mut self,ql:usize,qr:usize,v:isize) {
        self._update(ql,qr,0,self.size,0,v);
    }
    fn _update(&mut self,ql:usize,qr:usize,l:usize,r:usize,i:usize,v:isize) {
        self.eval(i, l, r);
        if qr<=l || r<=ql { return }
        if ql<=l && r<=qr {
            self.lazy[i] = v;
            self.eval(i, l, r);
        } else {
            self._update(ql,qr,l,(l+r)/2,2*i+1,v);
            self._update(ql,qr,(l+r)/2,r,2*i+2,v);
            self.nodes[i] = (self.fn_update)(self.nodes[2*i+1],self.nodes[2*i+2]);
        }
    }
}

fn main() {
    proconio::input!{
        (w,n):(usize,usize),
        blocks:[(usize,usize);n],
    }
    let size = w;
    let v = vec![0;w];
    let fn_get = |a:isize,b:isize|a.max(b);
    let fn_update = |a:isize,b:isize|a.max(b);
    let mut segtree = LazySegmentTree::new(size, v, 0, fn_get, fn_update);
    for i in 0..n {
        let (l,r) = blocks[i];
        let val = segtree.get(l,r+1);
        segtree.update(l,r+1,val+1);
        println!("{}",segtree.get(l,l+1));
    }
}
