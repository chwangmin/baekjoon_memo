import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int A, B;
    static int[][] map;

    static boolean[][] visited;

    static int answer1 = 0;
    static int answer2 = 0;

    static int[] nx = {1,-1,0,0};
    static int[] ny = {0,0,1,-1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        map = new int[A][B];

        visited = new boolean[A][B];

        for (int i = 0; i < A; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < B; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Deque<Point> queue = new LinkedList<>();

        for (int i = 0; i < A; i++) {
            for (int j = 0; j < B; j++) {
                if (visited[i][j] || map[i][j] == 0) {
                    continue;
                }

                visited[i][j] = true;
                answer1+=1;

                queue.add(new Point(i, j));

                int checkMax = 0;

                while(!queue.isEmpty()){
                    Point p = queue.pop();
                    checkMax++;

                    answer2 = Math.max(answer2, checkMax);

                    int x = p.x;
                    int y = p.y;

                    for (int k = 0; k < 4; k++){
                        int dx = x + nx[k];
                        int dy = y + ny[k];

                        if (dx < 0 || dy < 0 || dx >= A || dy >= B) {
                            continue;
                        }

                        if (visited[dx][dy]){
                            continue;
                        }

                        if (map[dx][dy] == 1){
                            queue.add(new Point(dx, dy));
                            visited[dx][dy] = true;
                        }
                    }
                }
            }
        }

        System.out.println(answer1);
        System.out.println(answer2);
    }
}
