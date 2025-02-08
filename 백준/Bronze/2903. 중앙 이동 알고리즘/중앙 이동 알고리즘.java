import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 등비수열 더하기
        int c = (int)(1*(Math.pow(2,N)-1));
        int result = (2+c)*(2+c);
        System.out.println(result);
    }
}