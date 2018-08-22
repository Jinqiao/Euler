import jq.euler.EulerUtil;

public class P27 {

	public static void main(String[] args) {

		int max = 0;


		for (int a = -999; a < 1000; a++)
			for (int b = -1000; b < 1001; b++)
			{
				int n = numP27Primes(a, b);

				if (n <= max) continue;
				max = n;
				System.out.format("max: {%d}, a: {%d}, b: {%d}\n", max, a, b);
			}

	}

	private static int numP27Primes(int a, int b){
		int n = 0;
		while(EulerUtil.isPrime(n * n + a * n + b )){
			n++;
		}
		return n;
	}
}
