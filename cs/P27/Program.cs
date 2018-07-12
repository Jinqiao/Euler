using System;
using EulerUtil;

namespace P27
{
    public class Program
    {
        public static void Main()
        {
            int max = 0;
            for (int a = -999; a < 1000; a++)
            for (int b = -1000; b < 1001; b++)
            {
                int n = NumP27Primes2(a, b);
                if (n <= max) continue;
                max = n;
                Console.WriteLine($"max: {max}, a: {a}, b: {b}");
            }

        }

        private static Func<int, int> GetP27Func(int a, int b)
        {
            return n => n * n + a * n + b;
        }

        private static int NumP27Primes(int a, int b)
        {
            int n = 0;
            var f = GetP27Func(a, b);
            while (f(n).IsPrime())
            {
                n++;
            }
            return n;
        }

        private static int NumP27Primes2(int a, int b)
        {
            int n = 0;
            while ((n * n + a * n + b).IsPrime())
            {
                n++;
            }
            return n;
        }
    }
}
