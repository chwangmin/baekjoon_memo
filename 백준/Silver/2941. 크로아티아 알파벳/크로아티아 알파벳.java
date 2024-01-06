import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();

        int answer = 0;

        for (int i = 0; i < word.length(); i++){
            answer++;
            if (word.charAt(i) == 'c'){
                if (i + 1 < word.length()){
                    if(word.charAt(i+1) == '=' || word.charAt(i+1) == '-'){
                        i++;
                    }
                }
            }
            else if (word.charAt(i) == 'd'){
                if (i + 1 < word.length()){
                    if (word.charAt(i+1) == '-'){
                        i++;
                    }
                    else if(word.charAt(i+1) == 'z'){
                        if (i + 2 < word.length()){
                            if(word.charAt(i+2) == '='){
                                i = i + 2;
                            }
                        }
                    }
                }
            }
            else if (word.charAt(i) == 'l'){
                if (i + 1 < word.length()){
                    if(word.charAt(i+1) == 'j'){
                        i++;
                    }
                }
            }
            else if (word.charAt(i) == 'n'){
                if (i + 1 < word.length()){
                    if(word.charAt(i+1) == 'j'){
                        i++;
                    }
                }
            }
            else if (word.charAt(i) == 's'){
                if (i + 1 < word.length()){
                    if(word.charAt(i+1) == '='){
                        i++;
                    }
                }
            }
            else if (word.charAt(i) == 'z'){
                if (i + 1 < word.length()){
                    if(word.charAt(i+1) == '='){
                        i++;
                    }
                }
            }
        }
        System.out.println(answer);

    }
}