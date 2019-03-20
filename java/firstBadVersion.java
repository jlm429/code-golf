public class firstBadVersion {

    private Boolean isBadVersion(int x) {
        boolean[] version = new boolean[5];
        version[0] = Boolean.FALSE;
        version[1] = Boolean.FALSE;
        version[2] = Boolean.FALSE;
        version[3] = Boolean.TRUE;
        version[4] = Boolean.TRUE;
        return version[x];
    }

    private int findBadVersionIter(int l, int r) {
        int m = 0;

        while (l <= r) {
            m = l + (r - l) / 2;
            if (isBadVersion(m - 1) == Boolean.FALSE && isBadVersion(m) == Boolean.TRUE) {
                return m;
            } else if (isBadVersion(m)) {
                //ignore right
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return -1;
    }

    private int findBadVersion(int low, int high){

        int mid = (low + high) /2;
        //int test = 1/2;
        //System.out.println(test);
        boolean checkMid = isBadVersion(mid);
        if (high<=low) {
            return low;
        }
        else if (mid<=low){
            return mid;
        }
        else if (checkMid && isBadVersion(mid-1)==Boolean.FALSE){
            return mid;
        }
        else if (checkMid){
            return findBadVersion(low, mid);
        }
        else{
            return findBadVersion(mid+1, high);
        }

    }

    public int firstBadVersion(int n){
        return this.findBadVersion(0, n);
    }
}
