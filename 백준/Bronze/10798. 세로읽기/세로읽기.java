import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[][] alphaArr = new char[5][15];

        for (int i = 0; i < 5; i++){
            String tmpSentence = sc.next();
            for (int j = 0; j < tmpSentence.length(); j++){
                alphaArr[i][j] = tmpSentence.charAt(j);
            }
        }
        for (int k = 0; k < 15; k++){
            for (int l = 0; l < 5; l++){
                if (alphaArr[l][k] == '\0') continue;
                System.out.print(alphaArr[l][k]);
            }
        }
    }
}