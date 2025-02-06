import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();
        int remain;

        while ( N > 0 ){
            remain = N%B;
            if (remain >= 10){ //A~Z (아스키:+55)
                sb.append((char)(remain+55));
            }else{
                sb.append((char)(remain+48));
            }
            N = N/B;
        }
        System.out.println(sb.reverse().toString());
    }
}