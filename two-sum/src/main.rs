use std::collections::HashMap;

fn main() {
    println!("{:?}", Solution::two_sum([2,7,11,15].to_vec(), 9));
    println!("{:?}", Solution::two_sum([3,2,4].to_vec(), 6));
    println!("{:?}", Solution::two_sum([3,3].to_vec(), 6));
}

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_map = HashMap::new();
        let mut searched_key;

        for (index, num) in nums.iter().enumerate() {
            searched_key = target - num;
            if num_map.contains_key(&searched_key) {
                return vec![*num_map.get(&searched_key).unwrap(), index as i32]
            } else {
                num_map.insert(num, index as i32);
            }
        }
        vec![0, 0]
    }
}
