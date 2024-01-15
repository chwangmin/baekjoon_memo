import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        int Q; int D; int N; int P;
        
        for (int i = 0; i < T; i++){
            Q = 0; D = 0; N = 0; P = 0;
            int C = sc.nextInt();

            while(C >= 25){
                C -= 25;

                Q++;
            }
            while(C >= 10){
                C -= 10;

                D++;
            }
            while(C >= 5){
                C -= 5;

                N++;
            }
            P = C;
            System.out.printf("%d %d %d %d\n",Q,D,N,P);
        }
    }
}