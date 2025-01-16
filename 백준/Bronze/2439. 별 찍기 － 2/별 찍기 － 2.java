import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < N; i++) {
            str.append("*");
            System.out.println(String.format("%" + N + "s", str));
        }
    }
}