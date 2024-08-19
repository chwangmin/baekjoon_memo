import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static long roomCnt, power;
    static long maxResult;
    static long result;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        roomCnt = Integer.parseInt(st.nextToken());
        power = Integer.parseInt(st.nextToken());

        result = 0;

        for (int i = 0; i < roomCnt; i++) {
            st = new StringTokenizer(br.readLine());

            long isEnemy = Integer.parseInt(st.nextToken());

            long first = Integer.parseInt(st.nextToken());
            long second = Integer.parseInt(st.nextToken());

            if (isEnemy == 1){
                enemyFunction(first, second);
            } else if (isEnemy == 2){
                potionFunction(first, second);
            }
        }
        System.out.println(maxResult + 1);
    }

    private static void enemyFunction(long first, long second){
        long tmp = (second - 1) / power;

        result += tmp * first;

        if (maxResult < result){
            maxResult = result;
        }
    }

    private static void potionFunction(long first, long second){
        power += first;
        if (result - second < 0){
            result = 0;
        } else {
            result -= second;
        }
    }
}