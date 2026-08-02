impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        // Linear Complexity
        // let k = nums.iter();
        // let mut val = 0;
        // for i in 0..=*k.max().unwrap(){
        //     val = i;
        //     if !nums.contains(&i){
        //         return i as i32;
        //     } 
        // }
        // return (val + 1) as i32

        // better solve
        return (0..=nums.len() as i32).sum::<i32>() - nums.iter().copied().sum::<i32>()        
        }
}