public class shiftzero {

    public static int[] shiftzeroes(int[] nums){
        int j = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0) {
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                j++;
            }
        }
        return nums;
    }

    public static int[] shiftzeroesBF(int[] nums){

        //bf solution
        for (int i=0; i<nums.length; i++){
            if (nums[i]==0){
                //shift
                for (int j=i; j<nums.length-1; j++){
                    nums[j]=nums[j+1];
                    nums[j+1]=-1;
                }
                i=i-1;
            }
        }

        for (int i=0; i<nums.length; i++){
            if (nums[i]==-1){
                nums[i]=0;
            }
        }

        return nums;

    }
}
