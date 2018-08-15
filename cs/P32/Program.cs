using System;
using System.Collections.Generic;
using System.Linq;
using static EulerUtil.U;

namespace P32
{
    public class Program
    {
        public static void Main()
        {
            int s = 0;
            for (int i = 0; i < 9999; i++)
            {
                if (IsPandigitalProd(i))
                {
                    // Console.WriteLine(i);
                    s += i;
                }
            }

            Console.WriteLine(s);
        }

        public static HashSet<List<int>> Subsets(List<int> factors)
        {
            // 1 << n <==> 2**n, because 1 << 4 = 10000 (as a binary number) = 16
            int n = factors.Count;
            var s = new HashSet<List<int>>(new MyListComparer());
            for (int i = 1; i < (1 << n) - 1; i++)
            {
                var l = new List<int>();
                for (int j = 0; j < n; j++)
                {
                    if ((i & (1 << j)) > 0)
                    {
                        l.Add(factors[j]);
                    }
                }

                s.Add(l);
            }

            return s;
        }

        public static HashSet<Tuple<int, int>> Split(int n)
        {
            var n1List = Subsets(n.Factors()).Select(l => l.Aggregate((a, x) => a * x)).Distinct();
            var result = new HashSet<Tuple<int, int>>();
            foreach (int n1 in n1List)
            {
                int n2 = n / n1;
                result.Add(new Tuple<int, int>(Math.Min(n1, n2), Math.Max(n1, n2)));
            }

            return result;
        }

        public static bool IsPandigitalProd(int n)
        {
            var s = Split(n);
            foreach (var pair in s)
            {
                string digitsStr = $"{pair.Item1}{pair.Item2}{n}";
                if (digitsStr.Length != 9 || digitsStr.Contains('0'))
                    continue;
                if (new HashSet<char>(digitsStr).Count == 9)
                {
                    // Console.WriteLine($"n1: {pair.Item1}, n2: {pair.Item2}");
                    return true;
                }
            }

            return false;
        }
    }

    public class MyListComparer : IEqualityComparer<List<int>>
    {
        public bool Equals(List<int> x, List<int> y)
        {
            if (x.Count != y.Count) return false;

            return !x.Where((t, i) => t != y[i]).Any();
        }

        public int GetHashCode(List<int> l)
        {
            return l.Sum();
        }
    }
}
