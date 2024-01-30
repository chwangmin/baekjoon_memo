
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int switchNum = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());

		int[] switchArr = new int[switchNum];

		int cntArr = 0;
		while (st.hasMoreTokens()) {
			switchArr[cntArr++] = Integer.parseInt(st.nextToken());
		}

		int studentNum = Integer.parseInt(br.readLine());

		for (int i = 0; i < studentNum; i++) {
			st = new StringTokenizer(br.readLine());
			int studentSex = Integer.parseInt(st.nextToken());
			int studentSelect = Integer.parseInt(st.nextToken());
			
			int tmpStudentSelect = studentSelect;
			
			if (studentSex == 1) {
				while (studentSelect <= switchNum) {
					if (switchArr[studentSelect - 1] == 0) {
						switchArr[studentSelect - 1] = 1;
					} else if (switchArr[studentSelect - 1] == 1) {
						switchArr[studentSelect - 1] = 0;
					}
					studentSelect += tmpStudentSelect;
				}
			} else if (studentSex == 2) {
				int cntSel = 1;
				if (switchArr[studentSelect - 1] == 0) {
					switchArr[studentSelect - 1] = 1;
				} else if (switchArr[studentSelect - 1] == 1) {
					switchArr[studentSelect - 1] = 0;
				}
				while (true) {//3-1 < 1 // 3+1 > 6
					int leftStudentSelect = studentSelect - 1 - cntSel;
					int rightStudentSelect = studentSelect - 1 + cntSel;
					
					if (leftStudentSelect < 0 || rightStudentSelect >= switchNum) {
						break;
					}
					
					if (switchArr[leftStudentSelect] == switchArr[rightStudentSelect]) {
						if (switchArr[leftStudentSelect] == 0) {
							switchArr[leftStudentSelect] = 1;
						} else if (switchArr[leftStudentSelect] == 1) {
							switchArr[leftStudentSelect] = 0;
						}
						if (switchArr[rightStudentSelect] == 0) {
							switchArr[rightStudentSelect] = 1;
						} else if (switchArr[rightStudentSelect] == 1) {
							switchArr[rightStudentSelect] = 0;
						}
					} else {
						break;
					}
					cntSel++;
				}
			}
		}
		for (int j = 0; j < switchNum; j++) {
			sb.append(switchArr[j]+" ");
			if((j+1)%20 == 0) {
				sb.append("\n");
			}
		}
		sb.deleteCharAt(sb.length()-1);
		System.out.print(sb);
	}
}