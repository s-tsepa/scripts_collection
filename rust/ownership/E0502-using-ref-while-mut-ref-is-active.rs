fn main () {
    let mut x: i64 = 42;
    let mut ref1 = &mut x;
    let ref2: &mut &mut i64 = &mut ref1;
    println!("{}", ref2);

    // In case ref2 is used later, use of ref1 fails. It's because the compiler infers that ref2 is used
    // later in code, so that use of any other (mut/const) ref is prohibited
    // Error: E0502
    println!("{}", ref1); // Error: cannot borrow `ref1` as immutable because it is also borrowed as mutable
    println!("{}", ref2); // mutable borrow later used here
}

