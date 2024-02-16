

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 
 * 말은 상하좌우 이동 가능 새로 이동한 칸에 적혀있는 알파벳은 지금까지와 달라야 visited 사용 최대한 몇칸을 이동할 수 있는지 작성
 * 알파벳 맵을 만을어 구현함. R, C 가 20 이니까 맵의 크기는 400*4int 1600 1.6KB 한칸으로 이동하고, 또 이동하는
 * 것이니깐 dfs로 구현 한칸마다 하나씩
 * 
 */

public class Main {
	static int R, C;
	static int[][] map;
	static int answer = 0;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		map = new int[R][C];
		visited = new boolean['Z' - 'A' + 1];

		for (int i = 0; i < R; i++) {
			String str = br.readLine();
			for (int j = 0; j < C; j++) {
				map[i][j] = str.charAt(j) - 'A';
			}
		}
		
		visited[map[0][0]] = true;
		dfs(0,0,1);
		
		System.out.println(answer);
	}

	static int[] dr = { 1, -1, 0, 0 };
	static int[] dc = { 0, 0, 1, -1 };

	/**
	 * 먼저 자신의 알파벳을 넣는다. 만약 주변에 잇는 것을 확인하고, 자신의 알파벳이라면 넘긴다.
	 * 
	 */

	static boolean[] visited;

	private static void dfs(int r, int c, int dist) {
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];
			if (nr < 0 || nr >= R || nc < 0 || nc >= C) {
				continue;
			}
			if (visited[map[nr][nc]]) {
				continue;
			}
			visited[map[nr][nc]] = true;
			dfs(nr, nc, dist + 1);
			visited[map[nr][nc]] = false;
		}
		if (dist > answer) {
			answer = dist;
		}
	}
}
