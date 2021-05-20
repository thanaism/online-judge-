use proconio::{input,marker::*};
const INF:i64 = 1<<60;
fn main(){
    input!{
        h:i64,w:i64,
        start:(Usize1,Usize1),
        goal:(Usize1,Usize1),
        grid:[Chars;h]
    }
    let di = vec![-1,0,1,0];
    let dj = vec![0,1,0,-1];
    let mut dist = vec![vec![vec![INF;4];1100];1100];
    let mut que = std::collections::VecDeque::new();
    let sx = start.0;
    let sy = start.1;
    for sz in 0..4 {
        dist[sx][sy][sz] = 0;
        que.push_back((sx,sy,sz));
    }
    while que.len()>0 {
        let (i,j,k) = que.pop_front().unwrap();
        for nz in 0..4 {
            let ni = i as i64 + di[k];
            let nj = j as i64 + dj[k];
            let mut now = dist[i][j][k];
            if k!=nz { now += 1 }
            if ni>=0 && ni<h && nj>=0 && nj<w {
                let nx = ni as usize;
                let ny = nj as usize;
                if grid[nx][ny]=='.' && dist[nx][ny][nz]>now {
                    dist[nx][ny][nz] = now;
                    if k!=nz { que.push_back((nx,ny,nz)) }
                    else { que.push_front((nx,ny,nz))}
                }
            }
        }
    }
    let mut ans = INF;
    let gx = goal.0;
    let gy = goal.1;
    for gz in 0..4 { ans = ans.min(dist[gx][gy][gz]) }
    println!("{}",ans);
}