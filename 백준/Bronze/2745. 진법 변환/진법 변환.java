import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String N = sc.next();
        int B = sc.nextInt();

        long result = 0;
        int idx = 0;
        int num = 0;
        for (int i = N.length()-1; i>= 0; i--){
            char c = N.charAt(i);
            if (c>='0' && c <='9')
                num = c - '0';
            else
                num = c - 'A' + 10;
            result += num * Math.pow(B,idx++);
        }
        System.out.println(result);
    }
}