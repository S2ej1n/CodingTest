import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int paperEA = Integer.parseInt(br.readLine());  //색종이 개수

        int[][] location = new int[100][100];
        int black = 0;
        for (int p = 0; p < paperEA; p++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            for (int j = n; j < n+10; j++) {
                for (int k = m; k < m+10; k++) {
                    location[j][k] = 1;
                }
            }
        }

        for (int j = 0; j < 100; j++) {
            for (int k = 0; k < 100; k++) {
                if (location[j][k] == 1) {
                    black++;
                }
            }
        }

        System.out.println(black);
    }
}