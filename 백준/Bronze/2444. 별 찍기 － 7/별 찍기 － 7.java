import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String s = "*"; String g = " ";

        for (int i = 1; i < N; i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(g.repeat(N-i));
            sb.append(s.repeat(2*i-1));
            System.out.println(sb.toString());
        }
        System.out.println(s.repeat(2*N-1));
        for (int i = 1; i < N; i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(g.repeat(i));
            sb.append(s.repeat(2*(N-i)-1));
            System.out.println(sb.toString());
        }
    }
}