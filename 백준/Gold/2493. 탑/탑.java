import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // br로 입력
		StringBuilder sb = new StringBuilder(); // sb에 출력 집어 넣기
		StringTokenizer st; // st 로 입력 나누기

		int N = Integer.parseInt(br.readLine()); // 숫자 값 넣기

		PriorityQueue<PointXY> heap = new PriorityQueue<PointXY>(); // 힙큐 사용 최소를 찾기 위해서

		int[] inputList = new int[N]; // 입력받을 숫자들 
		int[] answerList = new int[N]; // 답 리스트

		st = new StringTokenizer(br.readLine()); // st로 입력 줄 나누기 
		for (int i = 0; i < N; i++) { // 반복
			inputList[i] = Integer.parseInt(st.nextToken()); // 입력 받을 숫자들에 입력 넣기
		}

		heap.add(new PointXY(inputList[N-1], N-1)); // 맨 오른쪽에 있는 건물 그냥 먼저 넣기

		for (int i = N - 2; i >= 0; i--) { // 오른쪽에서 2번째 건물 부터 첫번째 까지.
			PointXY p = heap.peek(); // 현재 힙값 확인
			while (p != null && p.x < inputList[i]) { // p가 null이거나, p.x(heap에서 가장 작은 x) 가 현재 건물보다 작다면
				p = heap.poll(); // 그 값 빼기.
				answerList[p.y] = i+1; // 정답에 현재+1 을 넣기.
				p = heap.peek(); // 다시 힙에서 값 확인
			}
			heap.add(new PointXY(inputList[i],i)); // 현재 건물 힙큐에 넣기.
		}
		for (int k : answerList) { // 정답 리스트 확인
			sb.append(k+" "); // 정답 스트링빌더에 넣기
		}
		System.out.println(sb); // 출력
	}
	
	static class PointXY implements Comparable<PointXY>{ // 힙큐에 (x,y)를 한번에 넣기위해 만든 클래스
		private int x; // 건물 크기 부분
		private int y; // 건물 인덱스 부분
		
		public PointXY(int x, int y) { // 생성자 둘다 넣기.
			this.x = x; // 건물 크기 선언 
			this.y = y; // 건물 인덱스 선언
		}
		
		@Override
		public int compareTo(PointXY other) { // 비교할 때 
			return Integer.compare(this.x, other.x); // x를 기준으로 힙큐, 어차피 건물 크기는 다 다름.
		}
	}
	
}
