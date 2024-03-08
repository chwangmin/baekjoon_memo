import java.util.*;

class Solution {
    public static class Node{
        ArrayList<WeightEnd> endNode;
        Node(){
            endNode = new ArrayList<>();
        }
    }
    
    public static class WeightEnd implements Comparable<WeightEnd> {
        int w;
        int e;
        WeightEnd(int w, int e){
            this.w = w;
            this.e = e;
        }
        @Override
        public int compareTo(WeightEnd o){
            return Integer.compare(this.w, o.w);
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        
        Node[] nodes = new Node[N+1];
        
        boolean[] visited = new boolean[N+1];
        
        for (int i = 1 ; i < N+1; i++){
            nodes[i] = new Node();
        }
        
        for (int i = 0 ; i < road.length; i++){
            nodes[road[i][0]].endNode.add(new WeightEnd(road[i][2],road[i][1]));
            nodes[road[i][1]].endNode.add(new WeightEnd(road[i][2],road[i][0]));
        }
        
        Queue<WeightEnd> q = new PriorityQueue<>();
        
        q.add(new WeightEnd(0, 1));
        
        while(!q.isEmpty()){
            WeightEnd we = q.poll();
            
            int currentWeight = we.w;
            int currentNode = we.e;
            
            if (visited[currentNode]){
                continue;
            }
            
            visited[currentNode] = true;
            
            answer++;
            
            for (int i = 0 ; i < nodes[currentNode].endNode.size(); i++){
                int nextWeight = nodes[currentNode].endNode.get(i).w;
                int nextNode = nodes[currentNode].endNode.get(i).e;
                int sumWeight = currentWeight + nextWeight;
                
                if (sumWeight > K){
                    continue;
                }
                
                q.add(new WeightEnd(sumWeight,nextNode));
            }
        }

        return answer;
    }
    //양방향
//K시간 이하로 배달이 가능한 마을
//마을의 개수 ㅜ, 도로의 정보 road, 배달 가능한 시간 K
//음식 주문을 받을 수 있는 마을의 개수12
}