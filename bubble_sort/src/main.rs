use std::time::{Duration, Instant};
use rand::Rng;

fn main() {

    let mut v = generate_array();
    
    let now = Instant::now();
    bubble_sort(&mut v);
    let new_now = Instant::now();
    println!("Array sorted in {:?} seconds", new_now.duration_since(now));

    //print_array(&v);
    
}

fn bubble_sort(v: &mut [i32]){
    
    for _n in 1..v.len() {
    
        for i in 1..v.len() {
            if v[i -1 ] > v[i] {
                v.swap(i-1, i)
            }
        }
    }
}

fn print_array(array: &[i32] ){
    for (i, n) in array.iter().enumerate() {
        println!("Position {}: {}", i, n )
    }
}

fn generate_array() -> [i32; 10_000] {
    let mut v = [3; 10_000];
    
    for i in 0..v.len() {
        v[i] = rand::thread_rng().gen_range(1, 1001);
    }

    return v
}

