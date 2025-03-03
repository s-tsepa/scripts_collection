
#[cfg(test)]
mod tests {
    use containers::vector::Vector;
    use all_asserts::{assert_false};

    #[test]
    fn test_pop_till_empty() {
        let mut v = Vector::new(1, 3);
        assert_eq!(v.pop(), Some(1));
        assert_eq!(v.len, 2);
        assert_eq!(v.pop(), Some(1));
        assert_eq!(v.len, 1);
        assert_eq!(v.pop(), Some(1));
        assert_eq!(v.len, 0);
        assert_eq!(v.pop(), None);
    }

    #[test]
    fn test_insert() {
        let mut v = Vector::new(10, 5);
        assert_eq!(v.insert(6, 0), false);
        assert_eq!(v.insert(7, 0), false);
        assert_eq!(v.insert(3, 100), true);
        assert_eq!(v.insert(3, 100), true);
        assert_eq!(v.insert(0, 33), true);
    }

    #[test]
    fn test_insert_out_of_bounds() {
        let mut v = Vector::new(10, 5);
        assert_false!(v.insert(v.len, 100));
    }

    #[test]
    fn test_push_multiple() {
        let mut v = Vector::new(10, 5);

        assert_eq!(v.push(100), true);
        assert_eq!(v.len, 6);
        assert_eq!(v[v.len - 1], 100);
        assert_eq!(v.push(101), true);
        assert_eq!(v.len, 7);
        assert_eq!(v[v.len - 1], 101);
        assert_eq!(v.push(102), true);
        assert_eq!(v.len, 8);
        assert_eq!(v[v.len - 1], 102);
    }

    #[test]
    fn test_push_empty() {
        let mut v = Vector::new(0, 0);
        assert_eq!(v.push(1), true);
    }

    #[test]
    fn test_as_slice() {
        let mut v = Vector::new(1, 5);
        assert_eq!(v.as_slice(), &[1, 1, 1, 1, 1]);

        v.push(10);
        assert_eq!(v.as_slice(), &[1, 1, 1, 1, 1, 10]);

        v.push(10);
        assert_eq!(v.as_slice(), &[1, 1, 1, 1, 1, 10, 10]);

        v.insert(1, 3);
        assert_eq!(v.as_slice(), &[1, 3, 1, 1, 1, 1, 10, 10]);

        assert_eq!(v.pop(), Some(10));
        assert_eq!(v.as_slice(), &[1, 3, 1, 1, 1, 1, 10]);
    }
}
