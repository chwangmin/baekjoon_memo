class Solution {
    static int maxParkC;
    static int maxParkR;
    static char[][] staticPark;
    
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {};
        
        answer = new int[2];
        
        maxParkC = park.length;
        maxParkR = park[0].length();
        
        staticPark = new char[maxParkC][maxParkR];
        
        int currentC = 0;
        int currentR = 0;
        
        for (int i = 0; i < park.length; i++){
            for (int j = 0; j < park[0].length(); j++){
                staticPark[i][j] = park[i].charAt(j);
                if (staticPark[i][j] == 'S'){
                    currentC = i;
                    currentR = j;
                }
            }
        }
        
        for (String route: routes){
            String arrow = null;
            int num = 0;
            
            String[] routeSplit = route.split(" ");
            
            arrow = routeSplit[0];
            num = Integer.parseInt(routeSplit[1]);
            
            if (arrow.equals("N")){
                if(check(currentC-num, currentR)){
                      continue;
                }
                boolean isFlag = true;
                for (int j = 0; j < num ; j++){
                    if (staticPark[currentC-j][currentR] == 'X'){
                        isFlag = false;
                        break;
                    }
                }
                if (isFlag){
                    currentC -=num;
                }
            } else if (arrow.equals("S")){
                    if(check(currentC+num, currentR)){
                        continue;
                    }
                boolean isFlag = true;
                for (int j = 0; j < num ; j++){
                    if (staticPark[currentC+j][currentR] == 'X'){
                        isFlag = false;
                        break;
                    }
                }
                if (isFlag){
                    currentC +=num;
                }
            } else if (arrow.equals("W")){
                    if(check(currentC, currentR-num)){
                        continue;
                    }
                boolean isFlag = true;
                for (int j = 0; j < num ; j++){
                    if (staticPark[currentC][currentR-j] == 'X'){
                        isFlag = false;
                        break;
                    }
                }
                if (isFlag){
                    currentR -=num;
                }
            } else if (arrow.equals("E")){
                if(check(currentC, currentR+num)){
                        continue;
                }
                boolean isFlag = true;
                for (int j = 0; j < num ; j++){
                    if (staticPark[currentC][currentR+j] == 'X'){
                        isFlag = false;
                        break;
                    }
                }
                if (isFlag){
                    currentR +=num;
                }
            }
        }
        
        answer[0] = currentC;
        answer[1] = currentR;
        
        return answer;
    }
    
    public boolean check(int currentC, int currentR){
        if (currentC >= maxParkC || currentR >= maxParkR || currentC < 0 || currentR < 0){
            return true;
        }
        if (staticPark[currentC][currentR] == 'X'){
            return true;
        }
        return false;
    }
}