import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static ArrayList<Integer>[] list; // 리스트 배열을 사용해서 노드 각각에 연결 상태 입력하기.
	static boolean[] visited; // 방문 선언
	static StringBuilder sb = new StringBuilder(); //토크나이저
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //br로 빠르게 입력 받기
		StringTokenizer st = new StringTokenizer(br.readLine()); // ㅗ크나이저 하기
		
		int n = Integer.parseInt(st.nextToken()); // 첫번째 값 노드의 갯수
		int m = Integer.parseInt(st.nextToken()); // 두번째 값 간선의 갯수
		int v = Integer.parseInt(st.nextToken()); // 세번째 값 시작 노드

		list = new ArrayList[n+1]; // 리스트 크기 선언해주기
		visited = new boolean[n+1]; // 방문도 크기 선언해주기
		
		for (int i = 0 ; i < n+1 ; i++) { // list[i] 에 하나씩 넣기
			list[i] = new ArrayList<>();
		}
		
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			list[x].add(y);
			list[y].add(x);
		}
		
		for (int i = 0 ; i < n+1; i++) {
			Collections.sort(list[i]);
		}
		
		visited[v] = true;
		dfs(v);
		sb.append("\n");
		Arrays.fill(visited, false);
		visited[v] = true;
		bfs(v);
		System.out.println(sb);
	}
	
	static void dfs(int v) {
		sb.append(v).append(" ");
		for (int i = 0; i < list[v].size(); i++) {
			int tmp = list[v].get(i);
			if (visited[tmp]) {
				continue;
			}
			visited[tmp] = true;
			dfs(tmp);
		}
	}
	
	static void bfs(int v) {
		Queue<Integer> q = new ArrayDeque<>();
		
		q.add(v);
		while (!q.isEmpty()) {
			v = q.poll();
			sb.append(v).append(" ");
			for (int i = 0 ; i < list[v].size(); i++) {
				int tmp = list[v].get(i);
				if (visited[tmp]) {
					continue;
				}
				visited[tmp] = true;
				q.add(tmp);
			}
		}
	}
}
