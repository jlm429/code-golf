public class uniquePaths {

    public static int findUniquePaths(int m, int n){
        int[][] table=new int[m][n];
        for (int row=0; row<table.length; row++){
            for (int col=0; col<table[0].length; col++){
                if (row==0 || col == 0){
                    table[row][col]=1;
                }
                else{
                    table[row][col]=table[row-1][col]+table[row][col-1];
                }
            }
        }
        return table[m-1][n-1];
    }
}
