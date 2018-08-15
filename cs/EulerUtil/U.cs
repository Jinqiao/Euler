using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;

namespace EulerUtil
{
    [SuppressMessage("ReSharper", "UnusedMember.Global")]
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

        public static List<int> Factors(this int n)
        {
            int o = n = Math.Abs(n);
            int i = 2;
            double upBound = Math.Sqrt(n);
            var factors = new List<int>();
            while (i <= upBound && n > 1)
            {
                while (n % i == 0)
                {
                    factors.Add(i);
                    n /= i;
                }
                i += 1;
            }

            if (!factors.Any())
            {
                factors.Add(o);
                n = 1;
            }

            if (n > 1)
            {
                factors.Add(n);
            }

            return factors;
        }
    }
}
