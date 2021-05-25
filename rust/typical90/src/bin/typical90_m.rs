use proconio::{input,marker::Usize1};
fn main(){
    input!{
        (n,m):(usize,usize),
        graph:[(Usize1,Usize1,isize);m]
    }
    let mut edges = vec![Vec::new();n];
    for i in 0..m {
        let (a,b,c) = graph[i];
        edges[a].push((-c,b));
        edges[b].push((-c,a));
    }
    let mut dist_0 = vec![std::isize::MIN;n];
    dijkstra(&mut dist_0, 0, &edges);
    let mut dist_n = vec![std::isize::MIN;n];
    dijkstra(&mut dist_n, n-1, &edges);
    for i in 0..n {
        println!("{}",-dist_0[i]-dist_n[i]);
    }
}

fn dijkstra( dist:&mut Vec<isize>, start:usize, edges:&Vec<Vec<(isize,usize)>>) {
    dist[start]=0;
    let mut heap = std::collections::BinaryHeap::new();
    heap.push((0,start));
    while heap.len()>0 {
        let (c,i) = heap.pop().unwrap();
        for e in &edges[i] {
            let next = (c+e.0,e.1);
            if next.0 > dist[next.1] {
                heap.push(next);
                dist[next.1] = next.0;
            }
        }
    }
}