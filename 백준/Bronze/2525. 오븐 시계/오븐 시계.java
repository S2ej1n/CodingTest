import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(br.readLine());

        int h = (B + C)/60;
        int m = (B + C)%60;

        int fh = A + h;

        if (fh > 23){
            System.out.println(fh-24 +" "+ m);
        } else {
            System.out.println(fh+" "+ m);
        }
    }
}