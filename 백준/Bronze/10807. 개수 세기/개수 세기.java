import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        int N = sc.nextInt();
        int[] array = new int[N];
        for (int i=0;i<N;i++){
            array[i] = sc.nextInt();
        }
        int checkNum = sc.nextInt();
        for (int i = 0;i<N;i++){
            if (array[i] == checkNum){
                count++;
            }
        }

        sc.close();

        System.out.println(count);

    }
}