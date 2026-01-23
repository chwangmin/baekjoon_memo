import java.util.*;

class Solution {
    static int[][] staticMap;
    static boolean[][] visitMap;
    
    static Integer[] directionC;
    static Integer[] directionR;
    
    public int[] solution(String[] maps) {
        int[] answer = {};
        
        Deque<Integer> answer2 = new ArrayDeque<>();
        Deque<Integer[]> deque = new ArrayDeque<>();
        
        Integer[] directionC = new Integer[]{1,-1,0,0};
        Integer[] directionR = new Integer[]{0,0,1,-1};
        
        int c = maps.length;
        int r = maps[0].length();
        
        staticMap = new int[c][r];
        visitMap = new boolean[c][r];
        
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++){
                if (maps[i].charAt(j) == 'X'){
                    staticMap[i][j] = 0;
                    continue;
                }
                staticMap[i][j] = maps[i].charAt(j) - '0';
            }
        }
        
        for (int i = 0; i < c; i++){
             for (int j = 0; j < r; j++){
                 if (visitMap[i][j]){
                        continue;
                 }
                 if (staticMap[i][j] == 0){
                             continue;
                         }
                 deque.add(new Integer[]{i,j});
                int num = 0;
                 while(deque.size() != 0){
                      Integer[] current = deque.poll();
                     
                        int currentC = current[0];
                         int currentR = current[1];
                     
                        visitMap[currentC][currentR] = true;
                        num += staticMap[currentC][currentR];
                     
                     for (int d = 0; d < 4; d++) {
                         
                         int nextC = currentC + directionC[d];
                         int nextR = currentR + directionR[d];

                         if (nextC < 0 || nextR < 0 || nextC >= c || nextR >= r){
                             continue;
                         }

                         if (visitMap[nextC][nextR]){
                            continue;
                         }
                         
                         if (staticMap[nextC][nextR] == 0){
                             continue;
                         }
                         
                         visitMap[nextC][nextR] = true;
                         deque.add(new Integer[]{nextC, nextR});
                     }
                 }
                answer2.add(num);
              }
        }
        
        Integer[] answer3 = answer2.toArray(new Integer[0]);
        
        Arrays.sort(answer3);
        
        answer = new int[answer3.length];
        
        int idx=0;
        for (Integer val: answer3){
            answer[idx++] = val;
        }
        
        if (answer.length == 0){
            answer = new int[]{-1};
        }
        
        return answer;
    }
}