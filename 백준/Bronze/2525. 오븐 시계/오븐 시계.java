import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();

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