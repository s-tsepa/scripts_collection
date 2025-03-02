// pub mod chunks;

use std::fmt;
use crate::chunks as my;

#[derive(Debug)]
struct Vector<T: fmt::Display + Copy> {
    data: my::Chunks<T, true>,
    // len: usize,
    // capacity: usize,
}

impl<T: fmt::Display + Copy> Vector<T> {
    fn new(value: T, len: usize) -> Self {
        // TODO Safety: Needed?
        let chunks = unsafe { my::Chunks::filled(len, value) };
        Vector {
            data: chunks,
        }
    }
}
