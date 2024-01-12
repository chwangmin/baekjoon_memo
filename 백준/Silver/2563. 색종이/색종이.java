import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int colorPaperNum = sc.nextInt();

        int x = 0;
        int y = 0;

        int[][] drawingPaper = new int[100][100];
        
        for (int i = 0; i < colorPaperNum; i++) {
            x = sc.nextInt();
            y = sc.nextInt();

            for (int j = x; j < x+10; j++){
                for (int k = y; k < y+10; k++){
                    drawingPaper[j][k] = 1;
                }
            }
        }

        int answer = 0;
        
        for (int i = 0; i< 100; i++){
            for (int j = 0; j< 100; j++){
                if (drawingPaper[i][j] == 1) answer++;
            }
        }
        System.out.println(answer);
    }
}