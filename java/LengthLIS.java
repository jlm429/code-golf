import java.util.Arrays;
import java.util.Collections;

public class LengthLIS {

    public static int lengthOfLIS(int[] nums){
        if (nums.length==0){
            return 0;
        }

        //init table
        Integer[] table=new Integer[nums.length];
        table[0]=1;
        for (int i=1; i<table.length; i++){
            table[i]=1000;
        }

        int m;
        for (int i=1; i<nums.length; i++){
            m=0;
            for (int j=0; j<i; j++){
                if (nums[j]<nums[i]){
                    if (m<table[j]){
                        m=table[j];
                    }
                }
            }
            table[i]=1+m;
        }
        return Collections.max(Arrays.asList(table));
    }
}
