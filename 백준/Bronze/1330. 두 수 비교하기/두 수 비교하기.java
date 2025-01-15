import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        if ( A > B ) {
            System.out.println('>');
        } else if ( A < B ) {
            System.out.println('<');
        } else {
            System.out.println("==");
        }
    }
}