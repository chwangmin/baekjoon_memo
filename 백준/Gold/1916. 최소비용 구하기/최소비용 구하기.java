

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static class BUS implements Comparable<BUS>{
        int value;
        int end;

        BUS(int end, int value){
            this.end = end;
            this.value = value;
        }

        @Override
        public int compareTo(BUS o){
            return Integer.compare(this.value, o.value);
        }
    }
    static int N,M,answer;
    static ArrayList<ArrayList<BUS>> arr;

    static int[] visited;
    static boolean[] visited2;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        arr = new ArrayList<>();

        for (int i = 0 ; i < N + 1; i++){
            arr.add(new ArrayList<>());
        }

        int start, end, value;
        for (int i = 0 ; i < M; i++){
            st = new StringTokenizer(br.readLine());

            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());
            value = Integer.parseInt(st.nextToken());

            arr.get(start).add(new BUS(end,value));
        }

        st = new StringTokenizer(br.readLine());

        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        dijkstra(start);

        System.out.println(visited[end]);
    }

    static void dijkstra(int start){
        visited = new int[N + 1];
        visited2 = new boolean[N+1];

        Arrays.fill(visited,Integer.MAX_VALUE);

        PriorityQueue<BUS> pq = new PriorityQueue<>();

        pq.add(new BUS(start,0));
        visited[start] = 0;

        while(!pq.isEmpty()){
            BUS bus = pq.poll();
            int cur = bus.end;

            if (visited2[cur]) continue;

            visited2[cur] = true;

            int tmpValue;
            for (BUS tmpBus : arr.get(cur)){
                tmpValue = tmpBus.value + bus.value;

                if (tmpValue > visited[tmpBus.end]) continue;

                visited[tmpBus.end] = tmpValue;

                pq.add(new BUS(tmpBus.end, tmpValue));
            }
        }
    }
}
