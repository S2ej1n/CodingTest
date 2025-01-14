import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] tlist = input.split(" ");

        double A = Double.valueOf(tlist[0]);
        double B = Double.valueOf(tlist[1]);
        double result1 = A + B;
        double result2 = A - B;
        double result3 = A * B;
        double result4 = A / B;
        double result5 = A % B;
        System.out.println((int)result1);
        System.out.println((int)result2);
        System.out.println((int)result3);
        System.out.println((int)result4);
        System.out.println((int)result5);
    }
}