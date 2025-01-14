import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input," ");

        // 스트링으로 리턴값 고정되어있으므로 반드시 형변환 필요
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        System.out.println(A+B);
    }
}