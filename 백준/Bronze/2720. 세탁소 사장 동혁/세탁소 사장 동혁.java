import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int Q = 0, D = 0, N = 0, P = 0;

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int C = Integer.parseInt(st.nextToken());

            while (C >= 25){
                Q = C/25;
                C = C - 25*Q;
            }
            while (C >= 10){
                D = C/10;
                C = C - 10*D;
            }
            while (C >= 5){
                N = C/5;
                C = C - 5*N;
            }
            while (C >= 1){
                P = C/1;
                C = C - 1*P;
            }
            System.out.println(Q+" "+D+" "+N+" "+P);
            Q = 0; D = 0; N = 0; P = 0;
        }
    }
}