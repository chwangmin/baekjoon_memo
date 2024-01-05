import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();

        sc.close();

        int[] alphaArr = new int['z' - 'a' + 1];

        Arrays.fill(alphaArr, 0);

        char wordChar;
        
        for (int i=0; i < word.length(); i++){
            wordChar = word.charAt(i);
            if('a' <= wordChar){
                alphaArr[wordChar - 'a'] ++;
            } else{
                alphaArr[wordChar - 'A']++;
            }
        }

        int maxValue = 0;
        int maxCheckAlpha = 0;
        
        for (int i = 0; i < alphaArr.length;i++){
            if (maxValue < alphaArr[i]){
                maxValue = alphaArr[i];
                maxCheckAlpha = i;
            }
        }

        Arrays.sort(alphaArr);
        
        if (alphaArr['z' - 'a' - 1] == maxValue){
            System.out.println("?");
        } else {
            char answerAlpha = (char)('A' + maxCheckAlpha);
            System.out.println(answerAlpha);
        }
        
    }
}