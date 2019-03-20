public class removeDup {

    public static int removeDupsBF(int[] nums){
        //BF solution
        int count=0;
        for (int i=1; i<nums.length; i++){
            if (nums[i]==nums[i-1] && i<nums.length-count) {
                //shift
                count++;
                for (int j=i; j<nums.length-1;j++){
                    nums[j]=nums[j+1];
                }
                i--;
            }
        }
        return nums.length-count;
    }
    //O(n) solution
    public static int removeDups(int[] nums){

        //mark duplicates
        int j=0;
        int count=0;
        for (int i=1; i<nums.length; i++){
            if (nums[i]==nums[j]){
                nums[i]=-5000;
                count++;
            }
            else{
                j=i;
            }
        }

        //move to the end
        j=0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != -5000) {
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
                j++;
            }
        }

        return nums.length-count;
    }

    public static int removeDups2(int[] nums){


        //one pass solution
        int j = 1;
        for(int i = 0; i < nums.length-1; i++) {
            if(nums[i] != nums[i+1]) {
                nums[j]=nums[i+1];
                j++;
            }
        }
        return j;
    }
}
