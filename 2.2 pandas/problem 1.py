"""
С помощью анонимной lambda-функции создайте столбец "EurGrad", который переводит значения оценок столбца 'grade'  в европейскую систему.

Sample Input:
stud_id;Subject;grade
1;ТВиМС;60
2;МОР;70
3;ТВиМС;80
4;МОР;85
5;ТВиМС;100

Sample Output:
E D C B A
"""

import io
import sys
import pandas as pd


def check_mark(mark):
    if mark <= 60:
        return 'E'
    elif mark <= 70:
        return 'D'
    elif mark <= 80:
        return 'C'
    elif mark <= 85:
        return 'B'
    else:  # mark > 85
        return 'A'
    
    
table = sys.stdin.read()
df = pd.read_csv(io.StringIO(table), sep=';')

df['EurGrad'] = df['grade'].apply(check_mark)
# print(df)
'''
   stud_id Subject  grade EurGrad
0        1   ТВиМС     60     E
1        2     МОР     70     D
2        3   ТВиМС     80     C
3        4     МОР     85     B
4        5   ТВиМС    100     A
'''

print(*tuple(df['EurGrad']))
