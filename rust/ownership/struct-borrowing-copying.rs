use std::hint::black_box;

#[derive(Clone)]
#[derive(Copy)]
#[derive(Debug)]
struct A(u8);

fn print_generic<T: std::fmt::Debug>(x: T) {
    println!{"print_generic: {:?}", x};
}

fn print_generic_reference<T: std::fmt::Debug>(x: &T) {
    println!{"print_generic: {:?}", x};
}

fn print_value(a: A) {
    println!{"print_value: {:?}", a};
}

fn print_mut_value(mut a: A) {
    a.0 += 10;
    println!{"print_mut_value: {:?}", a};
}

fn print_reference(a: &A) {
    println!{"print_reference: {:?}", a};
}

fn print_mut_reference(a: &mut A) {
    a.0 += 100;
    println!{"print_mut_reference: {:?}", a};
}

fn main () {
    let mut a1: A = A ( 0 );
    println!{"A struct elem: {}", a1.0}

    // Using const reference: Works fine
    let a2: &A = &a1;
    println!{"A struct elem: {}", a2.0}
    black_box(a2);

    // Using mutable reference: Works fine
    let a3: &mut A = &mut a1;
    a3.0 += 1;
    println!{"A struct elem: {}", a3.0}
    /* Works fine: a3 is the active owner of the a1, so it can be taken by any reference
     */
    print_reference(a3);
    print_mut_reference(a3);

    /* A problem is that func tries to obtain 'a1' by some reference while another reference &mut (a3) is
     * active
     * === Error: E0502
     * cannot borrow `a1` as immutable because it is also borrowed as mutable
     */
    // print_reference(&a1);
    // let a4: A = *a2;

    // Works fine: It has `Copy` trait so all works fine
    print_value(*a3);

    /* Problem here is that compiler tries to treat full type T as "&mut A",
     * and it doesn't understand that it is reference type, so because it cannot infer `Copy` trait
     * for it, it moves it.
     * But this becomes a problem since a3 is used later
     * === Error: E0382
     * === Desc: move occurs because `a3` has type `&mut A`, which does not implement the `Copy` trait
     */
    // print_generic(a3);

    // Now works fine: Compiler understands that type is a reference, so it borrows value
    // print_generic_reference(a3);

    // Works fine: a3 is not moved, by rather passed-by-value, so outer value doesn't change
    let n1 = a3.0;
    print_mut_value(*a3);
    print_mut_value(*a3);
    assert!(n1 == a3.0);

    // Dereferencing reference of a type without Copy trait
    // === Error: E0507: consider implementing `Clone`/`Copy` trais for "A" type
    // let a4: A = *a3;
    // === Error: E0599: no method named `clone` found
    // let a4: A = *a3.clone();

    // Works fine
    let a4: A = a3.clone();
    println!{"A struct elem: {}", a4.0}
    // Moving value: fine
    print_value(a4);

    // Works fine
    let a5: A = *a3;
    println!{"A struct elem: {}", a5.0}
    // Moving value: fine
    print_value(a5);
}

