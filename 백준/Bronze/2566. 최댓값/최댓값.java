import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[9][9];

        int maxX = 0;
        int maxY = 0;
        int maxN = -1;

        for (int i = 0;i<9;i++){
            for (int j = 0; j<9;j++){
                arr[i][j] = sc.nextInt();
                if ( maxN < arr[i][j] ){
                    maxX = i + 1;
                    maxY = j + 1;
                    maxN = arr[i][j];
                }
            }
        }
        System.out.println(maxN);
        System.out.printf("%d %d", maxX, maxY);
    }
}