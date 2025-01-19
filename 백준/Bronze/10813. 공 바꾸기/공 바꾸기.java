import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] array = new int[N];
        for (int n = 0; n < N; n++) {
            array[n] = n+1;
        }

        int temp = 0;
        for (int l = 0; l < M; l++) {
            StringTokenizer item = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(item.nextToken());
            int j = Integer.parseInt(item.nextToken());
            temp = array[i-1];
            array[i-1] = array[j-1];
            array[j-1] = temp;
        }

        for (int h = 0; h < N; h++) {
            System.out.print(array[h] + " ");
        }
    }
}