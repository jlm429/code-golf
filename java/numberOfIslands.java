//recursive solution (can also do BFS)
public class numberOfIslands {

    private static void markIsland(char[][] grid, int i, int j, int numRows, int numCols) {
        //#North
        if (i-1>=0 && grid[i-1][j]=='1'){
            grid[i-1][j]='0';
            markIsland(grid, i-1,j,numRows,numCols);
        }
        //#South
        if (i+1<numRows && grid[i+1][j]=='1'){
            grid[i+1][j]='0';
            markIsland(grid, i+1,j,numRows,numCols);
        }
        //#East
        if (j-1>=0 && grid[i][j-1]=='1') {
            grid[i][j-1]='0';
            markIsland(grid, i,j-1,numRows,numCols);
        }
        //#West
        if (j+1<numCols && grid[i][j+1]=='1') {
            grid[i][j+1]='0';
            markIsland(grid, i,j+1,numRows,numCols);
        }
    }

    public static int numIslands(char[][] grid) {
        int numRows=grid.length;
        if (numRows==0){
            return 0;
        }
        int numCols=grid[0].length;
        int islands=0;
        for (int i=0; i<numRows; i++){
            for (int j=0; j<numCols; j++){
                if (grid[i][j]=='1'){
                    islands++;
                    markIsland(grid, i, j, numRows, numCols);
                }
            }
        }
        return islands;
    }
}
