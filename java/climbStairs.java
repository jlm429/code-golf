public class climbStairs {

    public static int countStairs(int n){
        if (n==1){
            return 1;
        }

        int first=1;
        int second=2;
        int total=2;
        for (int i=2; i<n; i++){
            total=first+second;
            first=second;
            second=total;
        }

        return total;
    }

}
