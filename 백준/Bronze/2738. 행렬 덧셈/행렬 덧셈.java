import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] A = new int[N][M];
        int[][] result = new int[N][M];

        for (int i = 0; i < N; i++) {
            StringTokenizer matrix = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                A[i][j] = Integer.parseInt(matrix.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            StringTokenizer matrix = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                result[i][j] = A[i][j] + Integer.parseInt(matrix.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}