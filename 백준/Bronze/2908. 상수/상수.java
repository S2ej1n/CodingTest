import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // StringBuilder는 String 타입을 인자로 받는다. 다른건 안됨.
        StringBuilder A = new StringBuilder(st.nextToken());
        StringBuilder B = new StringBuilder(st.nextToken());
        int a = Integer.parseInt(A.reverse().toString());
        int b = Integer.parseInt(B.reverse().toString());

        if(a>=b){
            System.out.println(a);
        }else {
            System.out.println(b);
        }
    }
}