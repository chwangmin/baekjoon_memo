import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();

        int n = sc.nextInt()-1;
        
        System.out.println(word.charAt(n));
        
        sc.close();
    }
}