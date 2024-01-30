
import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	final static int MAX_LADDER_SIZE = 100;
	static int[][] ladderMap = new int[MAX_LADDER_SIZE][MAX_LADDER_SIZE];
	static Point p = new Point(0, 0);
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {


		for (int testCase = 1; testCase < 11; testCase++) {
			br.readLine();
			
			inputLadderMap();
			findLadderStart(testCase, p.x, p.y);
		}
	}

	public static void inputLadderMap() throws IOException {
		for (int i = 0; i < 100; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 100; j++) {
				int tmpInt = Integer.parseInt(st.nextToken());
				ladderMap[i][j] = tmpInt;
				if (tmpInt == 2) {
					p.x = i;
					p.y = j;
				}
			}
		}
	}

	public static void findLadderStart(int testCase, int ladderX, int ladderY) {
		int[] arrowD = { -1, 1 };
		int arrow = 0;
		while (ladderX != 0) {
			if (arrow == 0) {
				ladderX -= 1;
				for (int i = 0; i < 2; i++) {
					int ny = ladderY + arrowD[i];
					if (ny < 0 || ny >= MAX_LADDER_SIZE) {
						continue;
					}
					if (ladderMap[ladderX][ny] == 1) {
						arrow = i + 1;
						break;
					}
				}
			} else if (arrow == 1) {
				if (ladderY - 1 < 0) {
					arrow = 0;
					continue;
				}
				if (ladderMap[ladderX][ladderY - 1] == 0) {
					arrow = 0;
					continue;
				}
				ladderY -= 1;
			} else if (arrow == 2) {
				if (ladderY + 1 >= MAX_LADDER_SIZE) {
					arrow = 0;
					continue;
				}
				if (ladderMap[ladderX][ladderY + 1] == 0) {
					arrow = 0;
					continue;
				}
				ladderY += 1;
			}
		}
		StringBuilder sb = new StringBuilder();
		sb.append("#" + testCase + " " + ladderY);
		System.out.println(sb);
	}
}
