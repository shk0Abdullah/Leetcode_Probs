impl Solution {
    pub fn find_missing_elements( nums: Vec<i32>) -> Vec<i32> {
        let mut range: Vec<i32> = (*nums.iter().min().unwrap()..*nums.iter().max().unwrap()).collect();
        range.retain( |&val| !nums.contains(&val)  );
        println!("{:?}", range);
        return range

    }
}