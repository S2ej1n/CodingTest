import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int first = scanner.nextInt();
        int second = scanner.nextInt();
        int result = 0;

        ArrayList<Integer> resultToken = new ArrayList<>();
        while( second > 0) {
            System.out.println(first * (second % 10));
            resultToken.add(first * (second % 10));
            second /= 10;
        }

        for ( int i = 0; i < resultToken.size(); i++) {
            result += (resultToken.get(i) * (int)Math.pow(10, i));
        }
        System.out.println(result);

    }
}