import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m, s, t;

    static class EDGE{
        int end;
        int weight;

        EDGE(int end, int weight){
            this.end = end;
            this.weight = weight;
        }
    }

    static ArrayList<ArrayList<EDGE>> arr = new ArrayList<>();

    static int[] distances;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0 ; i < n + 1; i++){
            arr.add(new ArrayList<>());
        }

        for (int i = 0 ; i < m; i++){
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            arr.get(start).add(new EDGE(end, weight));
            arr.get(end).add(new EDGE(start, weight));
        }

        st = new StringTokenizer(br.readLine());

        s = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());

        dijstra(s);

        System.out.println(distances[t]);
    }

    static void dijstra(int start){
        distances = new int[n + 1];

        Arrays.fill(distances, Integer.MAX_VALUE);

        distances[start] = 0;

        Deque<Integer> q = new LinkedList<>();

        q.add(start);

        while(!q.isEmpty()){
            int cur = q.poll();

            for (int i = 0; i < arr.get(cur).size(); i++){
                if(distances[arr.get(cur).get(i).end] > distances[cur] + arr.get(cur).get(i).weight){
                    distances[arr.get(cur).get(i).end] = distances[cur] + arr.get(cur).get(i).weight;
                    q.add(arr.get(cur).get(i).end);
                }
            }
        }
    }
}
