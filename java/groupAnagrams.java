import java.util.*;
public class groupAnagrams {
    public static List<List<String>> getGroupAnagrams(String[] strs) {
        Hashtable h=new Hashtable();
        LinkedList<String> temp;
        //hash string values
        for (int i=0; i<strs.length; i++){
            if (h.get(getStringKey(strs[i]))==null){
                temp=new LinkedList<>();
            }
            else {
                temp=(LinkedList<String>) h.get(getStringKey(strs[i]));
            }
            temp.push(strs[i]);
            h.put(getStringKey(strs[i]), temp);
        }
        return (List<List<String>>) (Object) getLists(h);
    }

    //for hash key
    private static String getStringKey(String str1){
        if (str1.length()>0){
            char[] chars=str1.toCharArray();
            Arrays.sort(chars);
            String str= "";
            for (int i=0; i<chars.length; i++){
                str=str+chars[i];
            }
            return str;
        }
        return "";
    }

    //get list of strings from each hash
    public static LinkedList<LinkedList<String>> getLists(Map mp) {
        LinkedList<LinkedList<String>> lists= new LinkedList();
        Iterator it = mp.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            lists.push((LinkedList<String>) pair.getValue());
        }
        return lists;
    }
}
