S = list(input())
cnt = 0
for i in range(len(S)-1):
  if S[i] == S[i+1]:
    cnt += 1
    S[i+1] = "0" if S[i+1] == "1" else "1"
print(cnt)



