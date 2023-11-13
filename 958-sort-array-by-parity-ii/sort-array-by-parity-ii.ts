function sortArrayByParityII(nums: number[]): number[] {
    
   let odd_ptr:number = 1;
   let even_ptr:number = 0;

    while(odd_ptr < nums.length && even_ptr < nums.length) {
        
        if (nums[odd_ptr] % 2 == 1) {
            odd_ptr += 2;
        } else if (nums[even_ptr] % 2 == 0) {
            even_ptr += 2;
        } else {
         const tmp = nums[even_ptr];
            nums[even_ptr] = nums[odd_ptr];
            nums[odd_ptr] = tmp;
        }
    }
    return nums;
};