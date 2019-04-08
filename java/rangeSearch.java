public class rangeSearch {

    public int[] rangeSearch(int[] nums, int target){
        int[] range=new int[2];
        range[0]=-1;
        range[1]=-1;
        int location= binarySearch(nums, 0, nums.length-1, target);
        if (location==-1){
            return range;
        }
        else{
            return getRange(nums, location);
        }
    }

    private int[] getRange(int[] nums, int location){
        int left=0;
        int right=nums.length-1;
        int[] range=new int[2];
        for (int i=location; i<nums.length-1; i++){
            if (nums[i+1]!=nums[i]){
                right=i;
                break;
            }
        }
        for (int i=location; i>0; i--){
            if (nums[i-1]!=nums[i]){
                left=i;
                break;
            }
        }
        range[0]=left;
        range[1]=right;
        return range;
    }

    private int binarySearch(int[] nums, int l, int r, int target){
        int m;
        while (l <= r) {
            m = l + (r - l) / 2;
            if (nums[m]==target) {
                return m;
            } else if (target<nums[m]) {
                //ignore right
                r = m - 1;
            } else {
                //ignore left
                l = m + 1;
            }
        }
        return -1;
    }
}
