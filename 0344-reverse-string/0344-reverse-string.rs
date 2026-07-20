impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut frwd_pointer = 0;
        let mut end_pointer = s.iter().len() -1;
        while (true){
            if (end_pointer > frwd_pointer){
                let temp = s[frwd_pointer]; // h
                s[frwd_pointer] = s[end_pointer]; // o at start
                s[end_pointer] = temp; // h at start
                frwd_pointer +=1;
                end_pointer -=1;
            }else{
                break
            }
        }
    }
}