public class P31
{
    private static final int[] coins = {1, 2, 5, 10, 20, 50, 100, 200};

    public static void main(String args[])
    {
        // for (int i = 0; i < args.length; i++) {
        //     System.out.format("%d : %s\n", i, args[i]);
        // }

        if(args.length == 0){
            System.out.format("Please enter amount\n");
            return;
        }

        int amount = Integer.parseInt(args[0]);
        System.out.format("Result is %d\n", ways(amount, 7));
        return;
    }

    private static int ways(int t, int i){
        if(i <= 0 || t == 0) return 1;

        int r = 0;
        while(t >= 0){
            r = r + ways(t, i - 1);
            t = t - coins[i];
        }
        return r;
    }
}
