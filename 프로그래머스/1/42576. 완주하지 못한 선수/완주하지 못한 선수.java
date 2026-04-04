import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> map = new HashMap<>();
        
        // 참가자 카운트
        for (int i = 0; i < participant.length; i++) {
            String curParticipant = participant[i];
            if (map.containsKey(curParticipant)) {
                map.put(curParticipant, map.get(curParticipant) + 1);
            } else {
                map.put(curParticipant, 1);
            }
        }
        
        // 완주자 제거
        for (int i = 0; i < completion.length; i++) {
            String curCompletion = completion[i];
            if (map.containsKey(curCompletion)) {
                map.put(curCompletion, map.get(curCompletion) - 1);
                if (map.get(curCompletion) == 0) {
                    map.remove(curCompletion);
                }
            }
        }
        
        // 남은 참가자가 답
        for (String key : map.keySet()) {
            answer = key;
        }
        
        return answer;
    }
}
