use std::collections::HashMap;

fn main() {
    println!("{}", Solution::contains_duplicate([1, 2, 3, 1].to_vec()));
    println!("{}", Solution::contains_duplicate([1, 2, 3, 4].to_vec()));
    println!("{}", Solution::contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2].to_vec()));
}


struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut number_mapping = HashMap::new();

        for num in &nums {
            if number_mapping.contains_key(&num) {
                return true;
            } else {
                number_mapping.insert(num, 1);
            }
        }

        return false;
    }
}
