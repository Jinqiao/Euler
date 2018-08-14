using System;

namespace P31
{
    class Program
    {
        static int[] coins = new int[] {1, 2, 5, 10, 20, 50, 100, 200};

        static void Main(string[] args)
        {
            if (args.Length == 0) {
                Console.WriteLine("Please enter amount");
            }

            int amount = int.Parse(args[0]);

            Console.WriteLine($"Result is {ways(amount, 7)}");

        }

        // t is target amount, i is current index in coins array(start from end)
        static int ways(int t, int i){
            if (i <= 0 || t == 0) {
                return 1;
            }

            int r = 0;
            while (t >= 0) {
                r = r + ways(t, i-1);
                t = t - coins[i];
            }
            return r;
        }
    }
}
