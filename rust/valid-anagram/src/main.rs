use std::collections::HashMap;

fn main() {
    println!("{}", Solution::is_anagram(String::from("anagram"), String::from("nagaram")));
    println!("{}", Solution::is_anagram(String::from("rat"), String::from("car")));
}

struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false
        }

        let mut char_map = HashMap::new();

        for index in 0..s.len() {
            let s_char = s.as_bytes()[index] as char;
            let t_char = t.as_bytes()[index] as char;

            char_map.entry(s_char).and_modify(|s_char| *s_char += 1).or_insert(1);
            char_map.entry(t_char).and_modify(|t_char| *t_char -= 1).or_insert(-1);
        }

        for (_, &value) in &char_map {
            if value != 0 {
                return false;
            }
        }

        true
    }
}
