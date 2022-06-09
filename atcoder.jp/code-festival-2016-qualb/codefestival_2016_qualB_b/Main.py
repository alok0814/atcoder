N,A,B = map(int, input().split())
S = list(input())
passed_num = 0
foreign_student_rank = 0

def is_student(str, A, B, passed_num, foreign_student_rank):
  if str == "a": 
    passed_num  = is_pass_domestic(A, B , passed_num)
  elif str == "b": 
    foreign_student_rank += 1
    passed_num  = is_pass_foreign(A, B, passed_num, foreign_student_rank)
  else : print('No')
  return passed_num, foreign_student_rank

def is_pass_domestic(A, B, passed_num):
  if passed_num < A+B:
    print('Yes')
    passed_num += 1
  else : print('No')
  return passed_num

def is_pass_foreign(A, B, passed_num, foreign_student_rank):
  if passed_num < A+B and foreign_student_rank <= B:
    print('Yes')
    passed_num += 1
  else : print('No')
  return passed_num

for s in S:
  # print(s, passed_num, foreign_student_rank)
  passed_num,foreign_student_rank = is_student(s, A, B, passed_num,foreign_student_rank) 