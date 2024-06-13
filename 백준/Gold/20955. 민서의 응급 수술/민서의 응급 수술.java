import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int n, m, answer;
    static int[] parentList;
    static boolean[] visited;

    static int allCheck = 1;

    static ArrayList<ArrayList<Integer>> linklist = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parentList = new int[n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < n + 1; i++) {
            parentList[i] = i;
            linklist.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if (findParent(x) == findParent(y)){
                answer++;
                continue;
            }

            unionParent(x, y);

            linklist.get(x).add(y);
            linklist.get(y).add(x);
        }

        checkLink();

        System.out.println(answer);
    }

    private static void checkLink() {
        visited[1] = true;

        int cur = 1;

        checkDfs(cur);

        for (int i = 1; i < n + 1; i++){
            if(!visited[i]){
                answer++;
                checkDfs(i);
            }
        }

    }

    private static void checkDfs(int cur) {
        visited[cur] = true;
        for (int x : linklist.get(cur)) {
            if (!visited[x]) {
                visited[x] = true;
                allCheck++;
                checkDfs(x);
            }
        }
    }

    private static void unionParent(int x, int y) {
        int parent1 = findParent(x);
        int parent2 = findParent(y);

        if (parent1 > parent2) {
            parentList[parent1] = parent2;
        } else {
            parentList[parent2] = parent1;
        }
    }

    private static int findParent(int x) {
        if(parentList[x] != x){
            parentList[x] = findParent(parentList[x]);
        }
        return parentList[x];
    }
    
    
}