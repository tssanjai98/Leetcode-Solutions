class Solution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        int[][] ans = new int[n][n];
        for(int[] query : queries){
            int rowStart = query[0];
            int rowEnd = query[2];
            int colStart = query[1];
            int colEnd = query[3];
            for(int i = rowStart;i<=rowEnd;i++){
                for(int j = colStart; j<=colEnd; j++){
                    ans[i][j] += 1;
                }
            }
        }
    return ans;
    }
}