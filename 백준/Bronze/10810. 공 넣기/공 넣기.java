import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] array = new int[N];

        for (int l = 0; l < M; l ++ ){
            StringTokenizer aitem = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(aitem.nextToken());
            int j = Integer.parseInt(aitem.nextToken());
            int k = Integer.parseInt(aitem.nextToken());

            for (int basket = i; basket <= j; ++basket){
                array[basket-1] = k;
            }
        }
        for (int h = 0; h < N; h ++ ){
            System.out.print((array[h] + " "));
        }
    }
}
