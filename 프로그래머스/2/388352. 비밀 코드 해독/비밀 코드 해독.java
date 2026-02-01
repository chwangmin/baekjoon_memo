import java.util.*;

class Solution {
    static List<Integer[]> answerList;
    static int maxSize, maxNum;
    static Integer[] arr;
    static boolean[] isNoAnswer;
    
    public int solution(int n, int[][] q, int[] ans) {
        int answer = 0;
        
        maxSize = 5;
        maxNum = n;
        
        answerList = new ArrayList<>();
        arr = new Integer[maxSize];
        
        dfs(1,0);
        
        isNoAnswer = new boolean[answerList.size()];
        
        for (int i = 0; i < ans.length; i++){
            for (int current = 0; current < answerList.size(); current++){
                Integer[] itg = answerList.get(current);
                if (isNoAnswer[current]){
                    continue;
                }
                int cnt = 0;
                for (int it : itg){
                    for (int j = 0; j < 5; j++){
                        if (it == q[i][j]){
                            cnt++;
                        }
                    }
                }
                if (cnt != ans[i]){
                    isNoAnswer[current] = true;
                }
            }
        }
        
        for (boolean check: isNoAnswer){
            if(!check){
                answer++;
            }
        }
        
        return answer;
    }
    
    static void dfs(int start, int currentSize){
        if (currentSize == maxSize){
            answerList.add(arr.clone());
            return;
        }
        for (int i = start; i <= maxNum; i++){
            arr[currentSize] = i;
            dfs(i+1, currentSize+1);
        }
    }
}

/* 131,950

시간 제한 사항 없음?

걍 해보기


*/