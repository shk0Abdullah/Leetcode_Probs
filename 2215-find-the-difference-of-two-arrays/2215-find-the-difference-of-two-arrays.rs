impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> { 
        let mut left:Vec<i32> = vec![];
        let mut right:Vec<i32> = vec![];
        {   for (i,k) in nums1.iter().enumerate(){
                if  !nums2.contains(k){
                    if !left.contains(k){
                        left.push(*k);
                    }
                }
            } 
        }

        for (i,k) in nums2.iter().enumerate(){
            if  !nums1.contains(k){
                if !right.contains(k){
                    right.push(*k);
                }
            }
        } 

        return vec![left,right];
    }
}