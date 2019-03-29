import java.util.Hashtable;

public class majorityElts {

    public static int majorityElement(int[] nums) {
        Hashtable table=new Hashtable();

        int temp=0;
        for (int i=0; i<nums.length; i++){
            if (table.get(nums[i])==null){
                table.put(nums[i], 1);
            }

            else {
                temp = (int) table.get(nums[i]);
                temp++;
                if (temp>(nums.length/2)){
                    return nums[i];
                }
                else{
                    table.put(nums[i], temp);
                }
            }
        }
        return -1;
    }
}
