// pub mod chunks;

use std::fmt;
use crate::chunks as my;

#[derive(Debug)]
struct Vector<T: fmt::Display + Copy> {
    data: my::Chunks<T>,
}

impl<T: fmt::Display + Copy> Vector<T> {
    fn new(value: T, len: usize) -> Self {
        // TODO wrap with safe checks
        unsafe {
            let mut v = Vector {
                data: my::Chunks::alloc(len)
            };
            v.data.memset(value);
            v
        }
    }
}
