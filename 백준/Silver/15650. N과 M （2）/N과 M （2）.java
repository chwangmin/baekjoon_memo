
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int maxNum, seqSize;
	static int[] nums;

	static void recur(int size, int start) { // 재귀 메소드
		if (size == seqSize) { // 사이즈가 맞다면 sb에 넣기.
			for (int i = 0; i < seqSize; i++) { // seqSize만큼 반복
				sb.append(nums[i]).append(" "); // nums의 해당 값을 넣기
			}
			sb.append("\n"); // 줄바꿈
			return; // 이 재귀 끝내기
		}

		for (int i = start; i < maxNum; i++) { // start 부터 시작해서 maxNum까지 - 0부터 하면 중복이 됨.
			nums[size] = i + 1; // 0부터 시작하기에 1 추가
			recur(size + 1, i + 1); // +1 하면서 재귀 i+1 부터 시작해야 중복 x 
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // br로 입력 받기
		StringTokenizer st; // 토크나이저 설정

		st = new StringTokenizer(br.readLine()); // 현재 입력 받은 값을 토큰화
		maxNum = Integer.parseInt(st.nextToken()); // 다음 토큰을 최대 숫자로
		seqSize = Integer.parseInt(st.nextToken()); // 다음 토큰을 seq 크기로 지정
		nums = new int[seqSize]; // nums 배열을 seq 크기로 지정

		recur(0, 0); //0,0부터 시작

		System.out.println(sb); // sb 모아놨던 것 출력하기.
	}
}
