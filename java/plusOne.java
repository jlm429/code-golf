public class plusOne {

    public static int[] doPlusOne(int[] digits){
        Boolean addOne=Boolean.FALSE;
        int last=digits.length-1;
        if (digits[last]<9){
            digits[last]++;
        }
        else{
            for (int i=last; i>=0; i--){
                if (digits[i]<9){
                    digits[i]++;
                    return digits;
                }
                else{
                    digits[i]=0;
                    if (i==0){
                        addOne=Boolean.TRUE;
                    }
                }
            }
        }

        if (addOne) {
            int[] temp=new int[digits.length+1];
            digits=temp;
            digits[0]=1;
        }

        return digits;
    }

}
