import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int num;
	static int answer;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		num = Integer.parseInt(br.readLine());
		answer = Integer.MAX_VALUE;

		dfs(0,num);

		System.out.println(answer);
	}

	private static void dfs(int cnt, int num) {
		if (num == 1) {
			answer = Math.min(cnt, answer);
		}

		if (cnt < answer) {
			if (num % 3 == 0) {
				dfs(cnt+1, num/3);
			}
			if (num % 2 == 0) {
				dfs(cnt+1, num/2);
			}
			dfs(cnt+1, num-1);
		}
	}
}
