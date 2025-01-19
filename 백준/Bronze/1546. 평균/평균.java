import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[N];
        double sum = 0.0;

        double M = Integer.MIN_VALUE;
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (arr[i] > M) {
                M = arr[i];
            }
        }

        for (int i = 0; i < N; i++) {
            sum += ((double)arr[i] / M) * 100;
        }
        System.out.println(sum/N);
    }
}