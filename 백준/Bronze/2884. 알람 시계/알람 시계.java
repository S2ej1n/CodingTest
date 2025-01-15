import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int M = scanner.nextInt();

        if ( H > 0 ) {
            if ( M >= 45) {
                M = M - 45;
                System.out.println(H +" "+ M);
            } else if ( M < 45) {
                H = H - 1;
                M = M + 15;
                System.out.println(H +" "+ M);
            }   
        } else if ( H == 0 ) {
            if ( M >= 45) {
                M = M - 45;
                System.out.println(H +" "+ M);
            } else if ( M < 45) {
                H = 23;
                M = M + 15;
                System.out.println(H +" "+ M);
            }
        }
    }
}