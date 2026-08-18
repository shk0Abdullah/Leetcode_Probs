impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let m = s.trim();
        let k: Vec<_> = m.split(" ").collect();
        println!("{:#?}", k);
        return k[k.len()-1].len() as i32
    }
}