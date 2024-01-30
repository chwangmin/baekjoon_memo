

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] switchArr; // 스위치 리스트를 전역으로 둔다.
	
	public static void switchRun(int studentSelect) { // 스위치가 동작했을 때 ss의 값을 0이면 1로 1이면 0으로 바꾼다. 
		if (switchArr[studentSelect ] == 0) { //해당 인덱스 value가 0이라면
			switchArr[studentSelect] = 1; // 해당 인덱스 value가 1로
		} else if (switchArr[studentSelect] == 1) { // 해당 인덱스 value가 1이라면
			switchArr[studentSelect] = 0; // 해당 인덱스 value가 0으로
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // br로 입력 값을 받는다.
		StringBuilder sb = new StringBuilder(); // sb로 출력 값을 한번에 저장해서 출력한다.

		int switchNum = Integer.parseInt(br.readLine()); // switch의 갯수를 받는다.
		
		switchArr = new int[switchNum]; // 스위치의 길이를 설정해준다

		StringTokenizer st = new StringTokenizer(br.readLine()); // 입력한 문장을 토크나이저를 사용하여 스위치의 리스트엥 각각 넣는다.

		int cntArr = 0; // 카운트를 0으로 초기화 한다.
		while (st.hasMoreTokens()) { // 입력 받은 토큰이 없을 때 까지 반복한다.
			switchArr[cntArr++] = Integer.parseInt(st.nextToken()); // 카운트를 올리며 토큰에 있던 값을 넣는다.
		}

		int studentNum = Integer.parseInt(br.readLine()); // 학생의 수를 입력 받는다.

		for (int i = 0; i < studentNum; i++) { // 학생의 수 만큼 반복한다.
			st = new StringTokenizer(br.readLine()); // 토크나이저를 통해 학생의 성별과, 학생이 선택한 수를 입력 받는다.
			int studentSex = Integer.parseInt(st.nextToken()); // 학생의 성별을 저장한다.
			int studentSelect = Integer.parseInt(st.nextToken()); // 학생이 선택한 수를 저장한다.
			
			int tmpStudentSelect = studentSelect; // 남학생을 위해 현재의 수를 임시 저장한다.
			
			if (studentSex == 1) { // 만약 남학생이라면
				while (studentSelect <= switchNum) { // student가 switchNum을 초과하지 않을 때 까지
					switchRun(studentSelect-1); // swtichRun을 진행한다.
					studentSelect += tmpStudentSelect; // studentSelect를 임시 저장한 값 만큼 추가한다.
				}
			} else if (studentSex == 2) { // 만약 여학생이라면
				int cntSel = 1; // cntSel을 1로 지정한다.
				switchRun(studentSelect - 1); // swtichRun을 진행한다.
				while (true) {//3-1 < 1 // 3+1 > 6
					int leftStudentSelect = studentSelect - 1 - cntSel; // 왼쪽의 값을 지정한다. 
					int rightStudentSelect = studentSelect - 1 + cntSel; // 오늘쪽의 값을 지정한다.
					
					if (leftStudentSelect < 0 || rightStudentSelect >= switchNum) { // 왼쪽과 오른쪽이 초과했다면
						break; // 반복문을 끝낸다.
					}
					
					if (switchArr[leftStudentSelect] == switchArr[rightStudentSelect]) { // 왼쪽과 오른쪽의 값이 같다면
						switchRun(leftStudentSelect); // swtichRun을 진행한다.
						switchRun(rightStudentSelect); // swtichRun을 진행한다.
					} else {
						break; // 멈추기
					}
					cntSel++; // cnt 를 1 추가해서 좌, 우로 1칸씩 움직인다.
				}
			}
		}
		for (int j = 0; j < switchNum; j++) { // 스위치 Arr을 출력하기 위해 반복
			sb.append(switchArr[j]+" "); // switchArr을 sb에 넣는다.
			if((j+1)%20 == 0) { // 20줄이 넘는다면 한줄 띄기
				sb.append("\n"); // sb에 한줄 띄기를 넣는다.
			}
		}
		sb.deleteCharAt(sb.length()-1); // 마지막 줄을 삭제한다.
		System.out.print(sb); // sb를 출력한다.
	}
}