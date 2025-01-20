import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] basket = new int[N];

        for (int n= 0; n < N; n++) {
            basket[n] = n + 1;
        }

        for (int l = 0; l < M; l++) {
            StringTokenizer range = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(range.nextToken()) - 1;
            int j = Integer.parseInt(range.nextToken()) - 1;

            reverse(basket, i, j);
        }
        for (int k = 0; k < N; k++) {
            System.out.print(basket[k]+" ");
        }
    }

    public static void reverse(int[] array, int start, int end) {
        while (start < end) {
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end --;
        }
    }
}