public class IncreasingTriplet {

    public boolean increasingTriplet(int[] nums) {
        if (nums.length<3){
            return Boolean.FALSE;
        }


        int first=Integer.MAX_VALUE;
        int second=Integer.MAX_VALUE;

        for (int i=0; i<nums.length; i++){
            if (nums[i]<=first){
                first=nums[i];
            }
            else if (nums[i]<=second){
                second=nums[i];
            }
            else {
                return Boolean.TRUE;
            }
        }
        return Boolean.FALSE; 
    }
}
