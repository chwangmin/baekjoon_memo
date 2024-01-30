
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder(); // StringBuilder로 출력
	static int numMax = 0; // numMax의 최댓값 설정 변수
	static int arrNum = 0; // arrNum의 최댓값 설정 변수
	static int[] answerArr; // 수열 답 리스트
	static boolean[] isSelected; // num을 선택했는지 확인 리스트 
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // br로 입력을 받는다.
		
		StringTokenizer st = new StringTokenizer(br.readLine()); // 입력을 받은 것을 나눈다.
		
		numMax = Integer.parseInt(st.nextToken()); // 첫번째를 numMax
		arrNum = Integer.parseInt(st.nextToken()); // 두번째를 arr의 크기로 설정한다.
		
		isSelected = new boolean[numMax+1]; // 선택한 것들을 저장하는 리스트에 대한 크기를 numMax+1을 해서 selected를 추가한다.
		answerArr = new int[arrNum]; // answerArr의 크기를 arrNum만큼 설정한다.
		
		recur(0); // 0부터 시작해서 찾는다.
		
		System.out.println(sb); // sb를 출력한다.
	}
	
	public static void recur(int num) {
		if (num == arrNum) { // 수열이 만들어 졌다면
			for (int i = 0 ; i < arrNum; i++) { // arrNum만큼 반복한다.				
				sb.append(answerArr[i] + " "); // answerArr[i]을 추가한다.
			}
			sb.append("\n"); // 마지막에는 줄바꿈 문자를 넣는다.
			return; // 재귀를 끝낸다.
		}
		for (int i = 1; i < numMax+1; i++) { // 1 ~ numMax + 1만큼 반복한다.
			if (isSelected[i] == true) {  // 만약 이미 선택된 숫자라면
				continue; // 그냥 넘긴다.
			}
			answerArr[num] = i; // 숫자를 답의 리스트에 넣는다.
			isSelected[i] = true; // 숫자 i 를 선택했다고 선언한다.
			recur(num+1); // 재귀를 다시 진행한다.
			isSelected[i] = false; // 숫자 i를 선택하지 않았다고 선언한다.
		 }
	}
}
