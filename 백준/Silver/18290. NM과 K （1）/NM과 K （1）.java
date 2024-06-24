import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int N, M, K;

    static int[][] map;

    static boolean[][] visited;

    static int answer;

    public static void main(String[] args) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer st = new StringTokenizer(br.readLine());

       N = Integer.parseInt(st.nextToken());
       M = Integer.parseInt(st.nextToken());
       K = Integer.parseInt(st.nextToken());

       map = new int[N][M];
       visited = new boolean[N][M];

       answer = Integer.MIN_VALUE;

       for (int i = 0; i < N; i++) {
           st = new StringTokenizer(br.readLine());
           for (int j = 0; j < M; j++) {
               map[i][j] = Integer.parseInt(st.nextToken());
           }
       }

       solve(0,0,0,0);
       System.out.println(answer);
    }

    private static void solve(int r, int c, int idx, int sum) {
        if(idx == K){
            answer = Math.max(answer, sum);
            return;
        }
        for (int i = r; i < N; i++) {
            for (int j = (i == r ? c : 0); j < M; j++) {
                if(visited[i][j]){
                    continue;
                }
                if(check(i,j)) {
                    visited[i][j] = true;
                    solve(i, 0, idx+1, sum + map[i][j]);
                    visited[i][j] = false;
                }
            }
        }
    }


    static int[] dr = {1,0,0,-1};
    static int[] dc = {0,-1,1,0};

    private static boolean check(int r, int c) {
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if(nr < 0 || nr >= N || nc < 0 || nc >= M){
                continue;
            }
            if (visited[nr][nc]) {
                return false;
            }
        }
        return true;
    }
}