import java.util.*;

class Solution {

    public int solution(int[][] points, int[][] routes) {
        int answer = 0;

        // time -> (cellKey -> count)
        Map<Integer, HashMap<Integer, Integer>> timeMap = new HashMap<>();

        for (int i = 0; i < routes.length; i++) {
            int curR = points[routes[i][0] - 1][0];
            int curC = points[routes[i][0] - 1][1];

            int time = 0;
            add(timeMap, time, curR, curC); // 시작(0초)

            for (int j = 1; j < routes[i].length; j++) {
                int endR = points[routes[i][j] - 1][0];
                int endC = points[routes[i][j] - 1][1];

                // r 먼저 이동
                while (curR != endR) {
                    if (curR < endR) curR++;
                    else curR--;
                    time++;
                    add(timeMap, time, curR, curC);
                }

                // c 이동
                while (curC != endC) {
                    if (curC < endC) curC++;
                    else curC--;
                    time++;
                    add(timeMap, time, curR, curC);
                }
            }
        }

        // 각 시간마다 위험 상황(같은 칸에 2대 이상) 개수 합산
        for (HashMap<Integer, Integer> cellCounts : timeMap.values()) {
            for (int cnt : cellCounts.values()) {
                if (cnt >= 2) answer++;
            }
        }

        return answer;
    }

    private void add(Map<Integer, HashMap<Integer, Integer>> timeMap, int time, int r, int c) {
        int key = r * 101 + c; // (r,c)를 1개의 정수로 압축 (r,c: 1..100)
        HashMap<Integer, Integer> m = timeMap.computeIfAbsent(time, t -> new HashMap<>());
        m.put(key, m.getOrDefault(key, 0) + 1);
    }
}
