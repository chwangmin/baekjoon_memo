

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int materialNum, sourList[], saltyList[];
	static boolean isSelected[];
	static int answer = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		materialNum = Integer.parseInt(br.readLine());
		sourList = new int[materialNum];
		saltyList = new int[materialNum];
		isSelected = new boolean[materialNum];
		
		for (int i = 0; i < materialNum; i++) {
			st = new StringTokenizer(br.readLine());
			sourList[i] = Integer.parseInt(st.nextToken());
			saltyList[i] = Integer.parseInt(st.nextToken());
		}

		generateSubSet(0, new int[]{-1,0});
		
		System.out.println(answer);
	}

	private static void generateSubSet(int cnt, int material[]) {
		if (cnt == materialNum) {
			if (material[1] == 0) {
				return;
			}
			int sum = Math.abs(Arrays.stream(material).sum());
			if (sum < answer) {
				answer = sum;
			}
			return;
		}
		generateSubSet(cnt + 1, new int[] {material[0] * sourList[cnt], material[1] + saltyList[cnt]});
		generateSubSet(cnt + 1, material);
	}
	
}
