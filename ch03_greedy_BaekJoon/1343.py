# chapter3 - greedy
# 1343번 - 폴리오미노

words = input()

words = words.replace('XXXX', 'AAAA')

words = words.replace('XX', 'BB')

if 'X' in words:
    print(-1)
    
else:
    print(words)
