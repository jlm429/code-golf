public class dpCoinChange {

    public static int coinChange(int[] coins, int amount) {
        int[] table = new int[amount+1];
        table[0]=0;

        //init table
        for (int i=1; i<table.length; i++){
            table[i]=1000;
        }

        int sub_res=0;
        for (int i=1; i<table.length; i++){
            for (int j=0; j<coins.length; j++){
                if (coins[j]<=amount && i-coins[j]>=0){
                    sub_res=table[i-coins[j]];
                    if (sub_res!=1000 && sub_res+1<table[i]){
                        table[i]=sub_res+1;
                    }
                }
            }
        }

        if (table[amount]==1000){
            return-1;
        }

        return table[amount];

    }
}
