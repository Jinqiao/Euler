using System;
using System.Linq;

namespace EulerUtil
{
    public static class U
    {
        // public static int[] SmallPrimes { get; } = {0, 1, 2, 3};

        public static bool IsPrime(this int n)
        {
            n = n > 0 ? n : -n;
            if(n == 0 || n == 1 || n == 2 || n == 3)
                return true;

            int i = 2;
            int ceil = (int)Math.Floor(Math.Sqrt(n));
            while (i <= ceil)
            {
                if (n % i == 0) return false;
                i++;
            }
            return true;
        }
    }
}
