class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        
        answer = new int[n*(n+1)/2];
        
        int[][] matrix = new int[n][n];
        
        int x = -1;
        int y = 0;
        
        int num = 1;
    
        for (int i = 0; i < n; i++){
           for (int j = i; j < n; j++){
               if (i % 3==0){
                   x++;
               } else if (i % 3 == 1){
                   y++;
               } else {
                   x--;
                   y--;
               }
               matrix[x][y] = num++;
           } 
        }
        
        int check = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                // System.out.print(matrix[i][j] + " ");
                
                if (matrix[i][j] == 0)
                    break;
                answer[check++] = matrix[i][j];
            }
            // System.out.println();
        }
        
        return answer;
    }
}