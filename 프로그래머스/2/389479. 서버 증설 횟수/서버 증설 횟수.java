import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        
        Deque<Integer[]> dq = new ArrayDeque<>();
        
        int maxPlayer = m;
        
        for (int cnt = 0; cnt < players.length; cnt++){
            int player = players[cnt];
            
            Integer[] check = dq.peek();
            
            if (check != null){
                if (check[1] <= cnt){
                    dq.pop();
                    maxPlayer -= check[0];
                }
            }
            
            if (player >= maxPlayer){
                System.out.println(player + " " + maxPlayer);
                int plusPlayer = ((player - (maxPlayer - m))/m) * m;
                System.out.println(plusPlayer);
                
                dq.add(new Integer[]{plusPlayer, cnt+k});
                
                maxPlayer += plusPlayer;
                
                answer += plusPlayer/m;
            }
            
            // System.out.println(answer);
        }
        
        return answer;
    }
}