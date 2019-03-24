import java.util.LinkedList;
import java.util.List;

public class groupAnagrams {

    public static void getGroupAnagrams(String[] strs) {


        byte[] temp1;
        byte[] temp2;

        //List<List<String>> return_list= new LinkedList();
        //List<String> temp=new LinkedList<>();

        //bit vector xor does not work - if str1 = ppp,  str2 = iii xor=0 but not an anagram
        //similar alternative - just add up ascii or byte values and compare
        // should be faster on avg. than most sorting algs.
        // }
        for (int i=0; i<strs.length-1; i++){
            System.out.print(strs[i]);
            System.out.print(strs[i+1]);
            System.out.println(checkAnagram(strs[i], strs[i+1]));
        }
    }

    private static Boolean checkAnagram(String str1, String str2){
        if (str1.length()==str2.length()){
            byte[] s1=str1.getBytes();
            byte[] s2=str2.getBytes();
            int b=0;
            int b2=0;
            for (int i=0; i<s1.length; i++){
                b=b+s1[i];
                b2=b2+s2[i];
            }
            if (b2==b){
                return Boolean.TRUE;
            }
        }
        return Boolean.FALSE;
    }
}
