import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String N = st.nextToken();
        int B = Integer.parseInt(st.nextToken());
        // 문자열 뒤집기
        StringBuffer sb = new StringBuffer(N);
        String n = sb.reverse().toString();

        char[] Narray = n.toCharArray();

        int num;
        int sum = 0;
        for (int i = 0; i < Narray.length; i++) {
            // 아스키
            num = (int)(Math.pow(B,i));
            if (Narray[i] >= 65) {
                int a = (Narray[i] - 55);
                sum += a*num;
            } else if (Narray[i] < 65) {
                int a = Narray[i] - 48;
                sum += a*num;
            }
        }
        System.out.println(sum);
    }
}