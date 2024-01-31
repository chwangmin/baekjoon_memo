import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	static int boardSize, numCnt;
	static int[][] board, sumBoard;
	static StringTokenizer st;
	static int x1, y1, x2, y2;
	static int answer;

	static void fillBoard() throws IOException {
		for (int i = 0; i < boardSize; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < boardSize; j++) {
				int tmpNum = Integer.parseInt(st.nextToken());
				board[i][j] = tmpNum;
				if (i == 0 && j == 0) {
					sumBoard[i][j] = tmpNum;
					continue;
				} else if (i == 0) {
					sumBoard[i][j] = sumBoard[i][j - 1] + tmpNum;
					continue;
				} else if (j == 0) {
					sumBoard[i][j] = sumBoard[i - 1][j] + tmpNum;
					continue;
				}
				sumBoard[i][j] = sumBoard[i - 1][j] + sumBoard[i][j - 1] + tmpNum - sumBoard[i-1][j-1];
			}
		}
	}

	static void calculBoard() {
		answer = 0;
		if (x1 == 0 && y1 == 0) {
			answer = sumBoard[x2][y2];
			return;
		} else if (x1 == 0) {
			answer = sumBoard[x2][y2] - sumBoard[x2][y1-1];
			return;
		} else if (y1 == 0) {
			answer = sumBoard[x2][y2] - sumBoard[x1-1][y2];
			return;
		} 
		answer = sumBoard[x2][y2] - sumBoard[x2][y1-1] - sumBoard[x1-1][y2] + sumBoard[x1-1][y1-1];
	}

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		boardSize = Integer.parseInt(st.nextToken());
		numCnt = Integer.parseInt(st.nextToken());
		board = new int[boardSize][boardSize];
		sumBoard = new int[boardSize][boardSize];

		fillBoard();

		for (int i = 0; i < numCnt; i++) {
			st = new StringTokenizer(br.readLine());
			x1 = Integer.parseInt(st.nextToken())-1;
			y1 = Integer.parseInt(st.nextToken())-1;
			x2 = Integer.parseInt(st.nextToken())-1;
			y2 = Integer.parseInt(st.nextToken())-1;
			
			calculBoard();
			
			sb.append(answer).append("\n");
		}
		System.out.println(sb);
	}
}
