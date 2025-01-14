import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] tlist = input.split(" ");

        int A = Integer.parseInt(tlist[0]);
        int B = Integer.parseInt(tlist[1]);
        System.out.println(A*B);
    }
}