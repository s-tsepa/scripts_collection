use std::alloc;
use std::ptr;
use std::fmt;
use std::ops::{Index, IndexMut};

pub struct Chunks<T>
where
    T: Copy
{
    pub ptr: *mut T,
    pub count: usize,
    pub allocated: bool,
    pub bounds_check: bool,
}

impl<T: Copy> Chunks<T> {
    pub unsafe fn alloc(count: usize) -> Self {
        let layout = alloc::Layout::array::<T>(count).unwrap();
        let ptr: *mut T = alloc::alloc(layout) as *mut T;
        Self {
            ptr,
            count,
            allocated: true,
            bounds_check: true
        }
    }

    pub unsafe fn dealloc(&mut self) {
        let layout = alloc::Layout::array::<T>(self.count).unwrap();
        let ptrByte = self.ptr as *mut u8;
        alloc::dealloc(ptrByte, layout);

        self.ptr = ptr::null::<T>() as *mut T;
        self.allocated = false;
    }

    pub unsafe fn memset(&mut self, value: T) {
        for i in 0..self.count {
            ptr::write(self.ptr.add(i), value);
        }
    }

    pub unsafe fn as_array<const N: usize>(&self) -> *const [T; N] {
        self.ptr as *const [T; N]
    }

    pub fn indices(&self) -> std::ops::Range<usize> {
        0..self.count
    }

    fn bounds(&self, index: usize) -> bool {
        match self.bounds_check {
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

        // Safety: Out-of-bounds is checked
        if self.bounds(index) {
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

impl<T: Copy> Index<usize> for Chunks<T> {
    type Output = T;

    fn index(&self, index: usize) -> &Self::Output {
        self.get(index).unwrap()
    }
}

impl<T: Copy> IndexMut<usize> for Chunks<T> {
    fn index_mut(&mut self, index: usize) -> &mut Self::Output {
        self.get_mut(index).unwrap()
    }
}

// ================== FMT ==================

impl<T: fmt::Display + Copy> fmt::Debug for Chunks<T> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Chunks: [");
        for i in 0..self.count {
            if i > 0 { write!(f, ", "); }
            let val: T = unsafe { self.ptr.add(i).read() };
            write!(f, "{}", val);
        }
        write!(f, "]")
    }
}

// ================== DROP ==================

impl<T: Copy> Drop for Chunks<T> {
    fn drop(&mut self) {
        if self.allocated {
            // Safety: We know we allocated this memory via `unsafe` so we must deallocate it.
            unsafe { self.dealloc(); }
        }
    }
}
