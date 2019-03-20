import java.util.Hashtable;

public class twosum {
    public static int[] getSum(int[] nums, int target){
        Hashtable h=new Hashtable();
        int[] nums2 = new int[2];

        //preprocess/hash nums
        for (int i=0; i<nums.length; i++){
            if (h.get(nums[i])==null) {
                h.put(nums[i], i);
            }
        }


        for (int i=0; i<nums.length; i++){
            if (h.get(target-nums[i])!=null){
                int temp= (int) h.get(target-nums[i]);
                if (i!=temp){
                    nums2[0]=i;
                    nums2[1]=temp;
                    //return nums2;
                }
            }
        }

        //h.forEach((k,v) -> System.out.println("key: "+k+" value:"+v));
        return nums2;
    }
}
