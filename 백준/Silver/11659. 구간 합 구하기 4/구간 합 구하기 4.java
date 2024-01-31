import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int numsSize, inputNum;
	static int[] nums;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int numsSize = Integer.parseInt(st.nextToken());
		int inputNum = Integer.parseInt(st.nextToken());
		int []nums = new int[numsSize];
		int []sumNums = new int[numsSize];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < numsSize; i++) {
			int tmpInt = Integer.parseInt(st.nextToken());
			nums[i] = tmpInt;
			if (i == 0) {
				sumNums[i] = tmpInt;
				continue;
			}
			sumNums[i] += sumNums[i-1] + tmpInt;
		}
		for (int i = 0; i < inputNum; i++) {
			st = new StringTokenizer(br.readLine());
			int left = Integer.parseInt(st.nextToken()) - 1;
			int right = Integer.parseInt(st.nextToken()) - 1;
			int answer = 0;
			
			if (left == 0) {
				answer = sumNums[right];
				sb.append(answer + "\n");
				continue;
			}
			
			int leftNum = sumNums[left - 1];
			int rightNum = sumNums[right];
			
			answer = rightNum - leftNum;
			
			sb.append(answer + "\n");
		}
		System.out.println(sb);
	}
}
