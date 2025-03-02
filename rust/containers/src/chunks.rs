use std::alloc;
use std::ptr;
use std::mem;
use std::fmt;
use std::ops::{Index, IndexMut};

type Layout = alloc::Layout;

fn array_layout<T>(count: usize) -> Layout {
    let layout = alloc::Layout::array::<T>(count).unwrap();
    assert_ne!(layout.size(), 0);
    assert_eq!(layout.size(), count * mem::size_of::<T>());
    layout
}

fn array_alloc<T>(count: usize) -> *mut T {
    let layout = array_layout::<T>(count);

    unsafe {
        alloc::alloc(layout) as *mut T
    }
}

fn array_realloc<T>(ptr: *mut T, count: usize, newCount: usize) -> *mut T {
    if (newCount == count) {
        return ptr;
    }

    let layout = array_layout::<T>(count);

    unsafe {
        alloc::realloc(
            ptr as *mut u8,
            layout,
            array_layout::<T>(newCount).size()
        ) as *mut T
    }
}

fn array_dealloc<T>(ptr: *mut T, count: usize) {
    // Safety: memory was allocated with same pointer and layout alignment
    unsafe {
        alloc::dealloc(
            ptr as *mut u8,
            array_layout::<T>(count)
        )
    }
}


pub struct Chunks<T, const BOUNDS_CHECK: bool = true, const AUTO_DROP: bool = true>
where
    T: Copy
{
    pub ptr: *mut T,
    pub count: usize,
}

impl<
    T: Copy,
    const BC: bool,
    const AD: bool,
> Chunks<T, BC, AD> {
    pub fn alloc(count: usize) -> Self {
        Self {
            ptr: array_alloc::<T>(count),
            count,
        }
    }

    pub unsafe fn filled(count: usize, value: T) -> Self {
        let mut c = Self::alloc(count);
        c.memset(value);
        c
    }

    pub fn dealloc(&mut self) {
        if self.allocated() {
            array_dealloc(self.ptr, self.count);
        }

        self.ptr = ptr::null::<T>() as *mut T;
        self.count = 0;
    }

    pub fn realloc(&mut self, newCount: usize) {
        if self.allocated() {
            self.ptr = array_realloc(self.ptr, self.count, newCount);
        } else {
            self.ptr = array_alloc(newCount);
        }
        self.count = newCount;
    }

    pub fn grow(&mut self, delta: usize) {
        if (!self.allocated()) {
            // Copy is in action? How efficiently?
            // self = Self::alloc(delta);
            return;
        }
        self.realloc(self.count + delta);
    }

    pub fn allocated(&self) -> bool {
        !self.ptr.is_null() && self.count > 0
    }

    pub unsafe fn memset(&mut self, value: T) {
        for i in 0..self.count {
            ptr::write(self.ptr.add(i), value);
        }
    }

    pub fn as_array<const N: usize>(&self) -> *const [T; N] {
        self.ptr as *const [T; N]
    }

    pub fn indices(&self) -> std::ops::Range<usize> {
        0..self.count
    }

    fn bounds(&self, index: usize) -> bool {
        match BC {
            false => true,
            true => 0 <= index && index < self.count,
        }
    }

    fn get(&self, index: usize) -> Result<&T, &'static str> {
        // Safety: Out-of-bounds is checked
        if self.bounds(index) {
            unsafe {
                // TODO Maybe return by reference?
                // Does &mut *... is a borrowing, i.e. moving?
                // Looks like overhead of moving twice
                Ok(&*self.ptr.add(index))
            }
        } else {
            Err("Index out of bounds")
        }
    }

    fn get_mut(&mut self, index: usize) -> Result<&mut T, &'static str> {
        // TODO Check overheads of such solution
        // May it be done better?
        //match self.get(index) {
        //    // === Error: [E0605]: non-primitive cast: `&T` as `&mut T`
        //    Ok(value) => Ok(value as &mut T),
        //    Err(err) => panic!("{}", err),
        //}

        if self.bounds(index) {
            // Safety: Out-of-bounds is checked
            unsafe {
                Ok(&mut *self.ptr.add(index))
            }
        } else {
            Err("Index out of bounds")
        }
    }
    // TODO is it right approach in Rust to have mut & const function's duplicates?
}

// ================== INDEX & INDEX_MUT ==================

impl<
    T: Copy,
    const BC: bool,
    const AD: bool,
> Index<usize> for Chunks<T, BC, AD> {
    type Output = T;

    fn index(&self, index: usize) -> &Self::Output {
        self.get(index).unwrap()
    }
}

impl<
    T: Copy,
    const BC: bool,
    const AD: bool,
> IndexMut<usize> for Chunks<T, BC, AD> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.get_mut(index).unwrap()
    }
}

// ================== FMT ==================

impl<
    T: fmt::Display + Copy,
    const BC: bool,
    const AD: bool,
> fmt::Debug for Chunks<T, BC, AD> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Chunks: [");
        for i in 0..self.count + 20 {
            if i > 0 { write!(f, ", "); }
            let val: T = unsafe { self.ptr.add(i).read() };
            write!(f, "{}", val);
        }
        write!(f, "]")
    }
}

// ================== DROP ==================

impl<
    T: Copy,
    const BC: bool,
    const AD: bool,
> Drop for Chunks<T, BC, AD> {
    fn drop(&mut self) {
        if self.allocated() && AD {
            // Safety: We know we allocated this memory via `unsafe` so we must deallocate it.
            unsafe { self.dealloc(); }
        }
    }
}
