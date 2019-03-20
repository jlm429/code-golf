public class reverseInt {

    public static int reverse(int x){
        String s = Integer.toString(x);
        char[] chars=s.toCharArray();
        Boolean neg=Boolean.FALSE;
        int end=chars.length;

        //check if negative
        if (chars[0]=='-'){
            neg=Boolean.TRUE;
            end=end-1;
        }

        //reverse
        char temp;
        for (int i=0; i<chars.length/2; i++){
            temp=chars[chars.length-i-1];
            chars[chars.length-i-1]=chars[i];
            chars[i]=temp;
        }

        //to string
        s="";
        for (int i=0; i<end; i++){
            s=s+chars[i];
        }

        //add sign and check for overflow
        double d=Double.valueOf(s);
        System.out.println(d);
        if (neg){
            if (d>Integer.MAX_VALUE){
                return 0;
            }
            d=d*-1;
        }

        else if (d>Integer.MAX_VALUE){
            return 0;
        }

        return (int)d;

    }
}
