import java.util.*;

public class topKFrequency {

    public static List<Integer> topKFrequent(int[] nums, int k){

        List<Integer> returnList = new LinkedList<>();

        //hash nums
        HashMap<Integer, Integer> hashMap=new HashMap();
        for (int i=0; i<nums.length; i++){
            int value = hashMap.get(nums[i])==null? 1 : (int) hashMap.get(nums[i]) + 1;
            hashMap.put(nums[i], value);
        }

        //using second hashmap (derp)
        HashMap<Integer, List<Integer>> secondMap=new HashMap();
        LinkedList<Integer> tempList;
        for (Map.Entry<Integer, Integer> entry: hashMap.entrySet()){
            if (secondMap.containsKey(entry.getValue())){
                secondMap.get(entry.getValue()).add(entry.getKey());
            }
            else {
                tempList=new LinkedList<>();
                tempList.add(entry.getKey());
                secondMap.put(entry.getValue(), tempList);
            }
        }

        //add top k to returnList
        for (int i=nums.length; i>0; i--) {
            if (k == 0) {
                return returnList;
            }
            if (secondMap.containsKey(i)) {
                for (int num : secondMap.get(i)) {
                    k--;
                    returnList.add(num);
                }
            }
        }

        return returnList;
    }

    //this part is a bit kludgy and slow, but can also be used instead
    //of second hashmap

    //Sort list of lists from hashmap and append top k elts to new list
    private static List<Integer> getTopK(HashMap hashMap, int k){
        LinkedList<LinkedList<Integer>> lists = new LinkedList<>();
        lists = getLists(hashMap);
        lists.sort((l1, l2) -> l1.get(0).compareTo(l2.get(0)));
        LinkedList<Integer> temp = new LinkedList<>();
        List<Integer> returnList = new LinkedList<>();
        for (int i=k-1; i>=0; i--){
            temp=lists.removeLast();
            returnList.add(temp.peekLast());
        }
        return returnList;
    }

    //get list of strings from each hash
    private static LinkedList<LinkedList<Integer>> getLists(Map mp) {
        LinkedList<LinkedList<Integer>> lists= new LinkedList();
        Iterator it = mp.entrySet().iterator();
        while (it.hasNext()) {
            LinkedList<Integer> list =new LinkedList<>();
            Map.Entry pair = (Map.Entry)it.next();
            list.push((int) pair.getKey());
            list.push((int) pair.getValue());
            lists.push(list);
        }
        return lists;
    }
}
