
macro_rules! test_parametrized {
    ($func_name:ident, $type_ident:ident, $type:ty) => {
        #[test]
        fn $type_ident() {
            return $func_name::<$type>();
        }
    }
}

#[cfg(test)]
mod tests {
    use containers::chunks::Chunks;
    use assert_panic::assert_panic;
    use std::alloc;
    use std::ptr;
    use std::mem;

    #[test]
    fn test_alloc_dealloc() {
        unsafe {
            let mut chunks = Chunks::<u32>::alloc(10);
            assert!(!chunks.ptr.is_null());
            chunks.dealloc();
            assert!(chunks.ptr.is_null());
        }
    }

    #[test]
    fn test_memset() {
        unsafe {
            let mut chunks = Chunks::<u32>::alloc(5);
            chunks.memset(42);
            for i in 0..5 {
                assert_eq!(*chunks.ptr.add(i), 42);
            }
        }
    }

    #[test]
    fn test_index() {
        unsafe {
            let mut chunks = Chunks::<u32>::alloc(3);
            chunks.memset(10);
            assert_eq!(chunks[0], 10);
            assert_eq!(chunks[1], 10);
            assert_eq!(chunks[2], 10);
        }
    }

    #[test]
    fn test_index_out_of_bounds() {
        unsafe {
            let mut chunks = Chunks::<u32>::alloc(3);
            chunks.memset(10);
            assert_eq!(chunks[0], 10);
            assert_eq!(chunks[1], 10);
            assert_eq!(chunks[2], 10);
            assert_panic!({ chunks[3]; });
        }
    }

    #[test]
    fn test_index_mut() {
        unsafe {
            let mut chunks = Chunks::<u32>::alloc(3);
            chunks.memset(5);
            chunks[1] = 99;
            assert_eq!(chunks[1], 99);
        }
    }

    #[test]
    fn test_as_array() {
        unsafe {
            let mut chunks = Chunks::<u32>::alloc(3);
            chunks.memset(7);
            let array_ptr = chunks.as_array::<3>();
            let array_ref = &*array_ptr;
            assert_eq!(array_ref, &[7, 7, 7]);
        }
    }

    fn test_reinterpret<T>() 
    where 
        T: Copy + std::fmt::Debug + std::cmp::PartialEq + From<u8>
    { unsafe {
        let SIZE = 20;
        let VALUE = 100;
        let size_factor: usize = mem::size_of::<T>() / mem::size_of::<u8>();
        let mut chunks = Chunks::<T>::alloc(SIZE);
        chunks.memset(VALUE.into());
        assert_eq!(chunks[0], VALUE.into());

        let ptr = chunks.ptr as *mut u8;
        let chunks2: Chunks<u8> = Chunks {
            ptr: ptr,
            count: SIZE * size_factor,
            // Double-free is possible, so do not treat it as allocated
            allocated: false,
            // Will exceed bounds intentionally further
            bounds_check: false,
        };

        /*
         * Checking that VALUE is present in first byte of each chunk
         */
        chunks2.indices().for_each(|i| {
            if i % size_factor == 0 {
                assert_eq!(chunks2[i], VALUE.into(), "(i: {i}) First byte in chunk is to be {VALUE}");
            } else {
                assert_eq!(chunks2[i], 0.into(), "(i: {i}) Rest part of chunk is to be 0");
            }
        });

        /*
         * Going out of array bounds by one more chunk, and check that VALUE is not present anymore
         */
        (0..size_factor).for_each(|i| {
            assert_ne!(chunks2[chunks2.count + i], VALUE, "(i: {i}) Chunk after array limit should not contain {VALUE}");
        });
    } }

    test_parametrized!(test_reinterpret, test_reinterpret_u8, u8);
    test_parametrized!(test_reinterpret, test_reinterpret_u16, u16);
    test_parametrized!(test_reinterpret, test_reinterpret_u32, u32);
    test_parametrized!(test_reinterpret, test_reinterpret_i16, i16);
    test_parametrized!(test_reinterpret, test_reinterpret_i32, i32);
    test_parametrized!(test_reinterpret, test_reinterpret_i64, i64);
}

