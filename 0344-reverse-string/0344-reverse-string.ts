/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    var frwd_pointer = 0
    var end_pointer = s.length-1
    while (true){
        if (end_pointer > frwd_pointer){
            var temp = s[end_pointer]; // o
            s[end_pointer] = s[frwd_pointer]; //h at end
            s[frwd_pointer] = temp; //o at start
            frwd_pointer +=1;
            end_pointer -=1;
            console.log(s);
        }else{
            break
        }
    }
};