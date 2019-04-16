public class RotatedArraySearch {

    public int search(int[] nums, int target){

        if (nums.length==0){
            return -1;
        }

        if (nums[0]<nums[nums.length-1]){
            return binarySearch(nums, 0, nums.length-1, target);
        }

        int m= nums.length/2;
        int left=-1;
        int right=-1;
        if (nums[m]==target){
            return m;
        }

        //binary search sorted half
        if (nums[0]<nums[m]){
            //binary search left
            left=binarySearch(nums,0,m,target);
            if (left!=-1){
                return left;
            }
            left=m+1;
            right=nums.length-1;
        }

        else {
            //binary search right half
            right=binarySearch(nums, m+1, nums.length-1, target);
            if (right!=-1){
                return right;
            }
            left=0;
            right=m;
        }

        while (left<=right){
            if (nums[left]==target){
                return left;
            }
            else if (nums[right]==target){
                return right;
            }
            else if (nums[left]<nums[right]){
                return binarySearch(nums, left, right, target);
            }
            left++;
            right--;
        }
        return -1;
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
