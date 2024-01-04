import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] checkNums = new int[]{1,1,2,2,2,8};

        int[] answer = new int[6];

        for (int i=0;i<6;i++){
            answer[i] = checkNums[i] - sc.nextInt();
            System.out.println(answer[i]);
        }
    }
}