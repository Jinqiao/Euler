from itertools import permutations

with open('py/data/p059_cipher.txt') as f:
    data = f.read()

ll = list(map(int, data.split(',')))
low_eng_range = range(ord('a'), ord('z') + 1)
# cap_eng_range = range(ord('A'), ord('Z') + 1)
# com_eng_list = list(low_eng_range) + list(cap_eng_range) + [32]
search_space = list(permutations(low_eng_range, 3))

max_cnt = 0
for cipher in search_space:
    i = 0
    sp_cnt = 0
    for n in ll:
        k = cipher[i % 3]
        i = i + 1
        # if (n ^ k) in com_eng_list:
        if (n ^ k) == 32:
            sp_cnt = sp_cnt + 1
    if sp_cnt > max_cnt:
        max_cnt = sp_cnt
        max_cipher = cipher

i = 0
msg_ls = []
for n in ll:
    k = max_cipher[i % 3]
    i = i + 1
    msg_ls.append(n ^ k)
msg = ''.join([chr(n) for n in msg_ls])
print(msg)
cipher_txt = ''.join([chr(n) for n in max_cipher])
print("the cipher is: " + cipher_txt)
print("sum of msg ascii:"  + str(sum(msg_ls)))
