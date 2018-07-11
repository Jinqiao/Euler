package jq.euler;

public class EulerUtil
{
    public static boolean isPrime(int n)
    {
        n = n > 0 ? n : -n;
        if(n == 0 || n == 1 || n == 2 || n == 3)
            return true;

        int i = 2;
        int ceil = (int)Math.floor(Math.sqrt(n));
        while (i <= ceil)
            {
                if (n % i == 0) return false;
                i++;
            }
        return true;
    }
}
