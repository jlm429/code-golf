public class maxSubArray {
    public static int maxSA(int[] nums){
        int maxValue=Integer.MIN_VALUE;
        int consecValue=0;
        for (int i=0; i<nums.length; i++){
            if (consecValue+nums[i]>=nums[i]){
                consecValue=nums[i]+consecValue;
            }
            else{
                consecValue=nums[i];
            }
            maxValue=java.lang.Math.max(consecValue, maxValue);
        }
        return maxValue;
    }
}
