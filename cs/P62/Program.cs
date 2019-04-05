using System;
using System.Collections.Generic;
using System.Linq;

namespace P62
{
    class Program
    {
        static Dictionary<string, List<long>> Dict { get; set; } = new Dictionary<string, List<long>>();

        static void Main(string[] args)
        {
            long i = 1;
            while (true)
            {
                i++;
                long c = i * i * i;
                string k = new string(c.ToString().OrderBy(c => c).ToArray());

                if (Dict.ContainsKey(k))
                {
                    var l = Dict[k];
                    l.Add(c);
                    if (l.Count() == 5)
                    {
                        foreach (long x in l)
                        {
                            Console.WriteLine($"k: {k}, c: {x}");
                        }
                        break;
                    }
                }
                else
                {
                    Dict[k] = new List<long> { c };
                }
            }
        }
    }
}
