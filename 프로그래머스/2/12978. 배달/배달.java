import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        boolean[] visited = new boolean[N + 1];
        int[] dist = new int[N+1];
        
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[1] = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        
        ArrayList<ArrayList<int[]>> arr = new ArrayList<>();
        
        for (int i = 0; i <= N; i ++){
            arr.add(new ArrayList<>());
        }
        
        for (int i = 0; i < road.length; i++){
            arr.get(road[i][0]).add(new int[]{road[i][1], road[i][2]});
            arr.get(road[i][1]).add(new int[]{road[i][0], road[i][2]});
        }
        
        // 첫번째가 현재 가중치, 두번째가 현재 노드
        pq.add(new int[]{0,1});
        
        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            
            if (visited[cur[1]]) continue;
            
            visited[cur[1]] = true;
            
            for (int[] next : arr.get(cur[1])){
                int nextNode = next[0];
                int nextWeight = next[1];
                
                int curWeight = cur[0] + nextWeight;
                if (dist[nextNode] > curWeight){
                    dist[nextNode] = curWeight;
                    pq.add(new int[]{curWeight, nextNode});
                }
            }
        }
        
        for (int distWeight: dist){
            if (distWeight <= K){
                answer++;
            }
        }
        
        

        return answer;
    }
}