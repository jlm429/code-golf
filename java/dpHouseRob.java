public class dpHouseRob {

    public static int rob(int[] nums){
        if (nums.length==0){
            return 0;
        }

        if (nums.length==1){
            return nums[0];
        }

        int first=nums[0];
        int second=java.lang.Math.max(nums[0], nums[1]);
        int total =java.lang.Math.max(nums[0], nums[1]);
        for (int i=2; i<nums.length; i++){
            total=java.lang.Math.max(nums[i]+first, second);
            first=second;
            second=total;
        }
        return total;
    }
}
