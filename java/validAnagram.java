public class validAnagram {

    public static Boolean checkStrings(String a, String b){

        //hash string a
        int[] nums=new int[Character.getNumericValue('z')-Character.getNumericValue('a')+1];
        for (int i=0; i<a.length(); i++){
            nums[Character.getNumericValue(a.charAt(i))-Character.getNumericValue('a')]++;
        }

        //check for each letter
        for (int i=0; i<b.length(); i++){
            if(nums[Character.getNumericValue(b.charAt(i))-Character.getNumericValue('a')]<=0){
                return Boolean.FALSE;
            }
            else{
                nums[Character.getNumericValue(b.charAt(i))-Character.getNumericValue('a')]--;
            }
        }

        //check if anagram
        for (int i=0; i<nums.length; i++){
            if (nums[i]>0){
                return Boolean.FALSE;
            }
        }

        return Boolean.TRUE;


    }
}
