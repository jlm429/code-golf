public class countPrimes {

    public static int sieve(int n){
        Boolean[] a=new Boolean[n];
        int sqrtN=(int) java.lang.Math.sqrt(n)+1;
        int count=n-2;
        //System.out.println(sqrtN);

        //init array
        a[0]=Boolean.FALSE;
        a[1]=Boolean.FALSE;
        for (int i=2; i<n; i++){
            a[i]=Boolean.TRUE;
        }

        for (int i=2; i<sqrtN; i++){
            if(a[i]){
                for (int j=(int)java.lang.Math.pow(i,2); j<n; j=j+i){
                    if (a[j]){
                        count--;
                    }
                    a[j]=Boolean.FALSE;

                }
            }
        }

        //count TRUE
/*        int numPrimes=0;
        for (int i=0; i<n; i++){
            if (a[i]){
                System.out.println(i);
                numPrimes++;
            }
        }*/

        return count;
    }

}
