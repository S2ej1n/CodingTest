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
        double result = A / B;
        System.out.println(result);
    }
}