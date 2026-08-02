use std::collections::HashSet;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        // quadratic Complexity
        // for (ind_first, i) in nums.iter().enumerate(){
        //     for (ind, j) in nums.iter().enumerate(){
        //         if i == j && ind_first != ind{
        //             return true
        //         }
        //     }
        // }

        // return false

        // Linear Complexity
        let x: HashSet<_> = nums.iter().collect();
        if x.len() == nums.len(){
            return false;
        }
        return true;   
    }
}