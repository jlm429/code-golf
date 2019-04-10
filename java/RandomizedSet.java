import java.util.HashMap;

class RandomizedSet {

    private HashMap<Integer, Integer> first=new HashMap();
    private HashMap<Integer, Integer> second=new HashMap();

    /** Initialize your data structure here. */
    public RandomizedSet() {

    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element.*/
    public boolean insert(int val) {
        if (this.first.containsKey(val)){
            return Boolean.FALSE;
        }
        else {
            this.first.put(val, this.first.size());
            this.second.put(this.first.size()-1, val);
            return Boolean.TRUE;
        }
    }

    /** Removes a value from the set. Returns true if the set contained the specified element.*/
    public boolean remove(int val) {
        if (this.first.containsKey(val)){
            int secondKey=this.first.get(val);
            this.first.remove(val);
            this.second.put(secondKey, this.second.get(this.second.size()-1));
            if (this.first.size()>0 && secondKey<this.first.size()){
                this.first.put(this.second.get(this.second.size()-1), secondKey);
            }
            this.second.remove(this.second.size()-1);
            return Boolean.TRUE;
        }
        return Boolean.FALSE;
    }

    /** Get a random element from the set. */
    public int getRandom() {
        int r=(int) (Math.random()* (this.first.size()));
        return this.second.get(r);
    }
}