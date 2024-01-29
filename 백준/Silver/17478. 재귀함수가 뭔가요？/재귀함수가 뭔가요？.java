
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringBuilder sb = new StringBuilder();
	static String s1 = "\"재귀함수가 뭔가요?\"\n";
	static String s2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n";
	static String s3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n";
	static String s4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n";
	static String s5 = "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n";
	static String s6 = "라고 답변하였지.\n";

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		sb.append("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n");
		dfs(N, 0);
		System.out.print(sb);
	}

	static public void dfs(int count, int cnt_) throws IOException {
		StringBuilder sb_ = new StringBuilder();
		
		for (int i = 0; i < cnt_; i++) {
			sb_.append("____");
		}
		
		if (count == 0) {
			sb.append(sb_).append(s1);
			sb.append(sb_).append(s5);
			sb.append(sb_).append(s6);
			return;
		}
		sb.append(sb_).append(s1);
		sb.append(sb_).append(s2);
		sb.append(sb_).append(s3);
		sb.append(sb_).append(s4);
		dfs(count - 1, cnt_ + 1);
		sb.append(sb_).append(s6);
		return;
	}
}
