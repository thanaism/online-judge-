struct Prim {}
impl Prim {
    fn init(graph: Vec<Vec<isize>>){
        println!("{:?}",graph);
    }
}
fn main(){
    Prim::init(vec![vec![0;1];1]);
}