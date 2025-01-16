import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        int[] list = new int[T];

        for (int i = 0; i < T; i++) {
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            list[i] = A+B;
        }

        for (int i = 0; i < T; i++) {
            System.out.println(list[i]);
        }
    }
}