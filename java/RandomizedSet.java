import java.util.HashMap;


/*
Optimized Solution using 2 hash tables.
The first hash table (first) contains the set val as key and index in the second
hash table (second) as values.  The second hash table allows random access to stored
values using the getRandom method.  Keys are maintained as a contiguous set of integers.
When a value is removed, if there is more than one value in the set, the last value is
re-inserted into the hash table and it's corresponding index in the first is changed.

Example:

insert 1 True
insert 3 True
First Hash Table {1: 0, 3: 1}
Second Hash Table {0: 1, 1: 3}
remove 1 (re-insert 3 in second and change index in first)
First Hash Table {3: 0}
Second Hash Table {0: 3}


 */
class RandomizedSet {

    private HashMap<Integer, Integer> first=new HashMap();
    private HashMap<Integer, Integer> second=new HashMap();

    /** Constructor */
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