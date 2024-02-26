import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static class Work {
		int reward;
		int time;

		public Work(int reward, int time) {
			super();
			this.reward = reward;
			this.time = time;
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = null;

		Deque<Work> q = new ArrayDeque<>();
		int N = Integer.parseInt(br.readLine());
		int answer = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int command = Integer.parseInt(st.nextToken());
			if (command == 0) {
				if (q.isEmpty()) {
					continue;
				}
				Work w = q.poll();
				if (--w.time == 0) { // time이 1이었다면,
					answer += w.reward;
					continue;
				}
				q.addFirst(new Work(w.reward, w.time));
			} else { // command == 1
				int reward = Integer.parseInt(st.nextToken());
				int time = Integer.parseInt(st.nextToken());
				if (--time == 0) { // time이 1이었다면,
					answer += reward;
					continue;
				}
				q.addFirst(new Work(reward, time));
			}
		}
		sb.append(answer).append("\n");

		System.out.println(sb);
	}
}
