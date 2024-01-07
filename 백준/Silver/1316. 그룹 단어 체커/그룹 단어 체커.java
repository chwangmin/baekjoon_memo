import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int wordNum = sc.nextInt();

        String word;

        int wordArrCheck[] = new int['z'-'a'+1];

        int answer = 0;

        int wordGroupCheck;

        char prev = ' ';

        for (int i = 0; i < wordNum; i++){
            word = sc.next();
            wordGroupCheck = 1;
            Arrays.fill(wordArrCheck,0);
            for (int j = 0; j < word.length(); j++){
                if (wordArrCheck[word.charAt(j) - 'a'] == 0 || prev == word.charAt(j)) {
                    wordArrCheck[word.charAt(j) - 'a']++;
                    prev = word.charAt(j);
                } else {
                    wordGroupCheck = 0;
                    break;
                }
            }
            if (wordGroupCheck == 1) {
                answer++;
            }
        }
        System.out.println(answer);
    }
}