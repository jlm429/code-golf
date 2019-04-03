public class dpCanJump {

    public static Boolean canJump(int[] nums){
        if (nums.length<=1){
            return Boolean.TRUE;
        }
        if (nums[0]==0){
            return Boolean.FALSE;
        }
        int current;
        int prev=nums[0];
        for (int i=0; i<nums.length-1; i++){
            current=java.lang.Math.max(prev-1, nums[i]);
            if (current==0){
                return Boolean.FALSE;
            }
            prev=current;
        }
        return Boolean.TRUE;
    }



}
