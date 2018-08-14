# a example of generator
# def squares(n=10):
#     for i in xrange(1, n+1):
#         print('Generating squares from 1 to {}'.format(n**2))
#         yield i ** 2


# gen = squares()
# for x in gen:
#     print(x)


coins = [1, 2, 5, 10, 20, 50, 100, 200]


def make_change(amount, hand=None):
    hand = [] if hand is None else hand
    if amount == 0:
        yield hand
    for coin in coins:
        if coin > amount or (len(hand) > 0 and hand[-1] < coin):
            continue
        for result in make_change(amount - coin,
                                  hand=hand + [coin]):
            yield result


changes = make_change(200)
ways = 0
for x in changes:
    ways = ways + 1
print(ways)
