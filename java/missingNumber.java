public class missingNumber {

    public static int findNumber(int[] nums){

        //simple 2 pass solution
        int[] nums2=new int[nums.length+1];

        //hash nums
        for (int i=0; i<nums.length; i++){
            nums2[nums[i]]=1;
        }

        //find missing nums
        for (int i=0; i<nums2.length; i++){
            if (nums2[i]==0){
                return i;
            }
        }
        return -1;
    }
}
