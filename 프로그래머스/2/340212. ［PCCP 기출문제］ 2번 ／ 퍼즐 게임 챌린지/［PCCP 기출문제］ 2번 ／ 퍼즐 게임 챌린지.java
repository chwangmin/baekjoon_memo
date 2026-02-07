import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        
        int start = 1;
        int end = Arrays.stream(diffs).max().getAsInt();
        
        int half = 0;
        
        while (start <= end){
            half = (start + end) / 2;
        
            long totalTime = 0;
            
            for (int i = 0; i < diffs.length; i++){
                int curTime = times[i];
                
                int timePrev = 0;
                
                if (i > 0){
                    timePrev = times[i-1];
                }
                
                int curReplay = diffs[i] - half;
                
                if (curReplay > 0){
                    totalTime += (timePrev + curTime) * curReplay + curTime;
                    continue;
                }
                
                totalTime += curTime;
            }
            
            if (totalTime <= limit){
                answer = half;
                end = half - 1;
                continue;
            }
            start = half + 1;
        }
        
        return answer;
    }
}