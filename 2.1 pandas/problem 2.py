"""
Вычислите среднее значение столбца 'grade'

Sample Input:
stud_id; Subject; grade
1;ТВиМС;60
2;МОР;70
3;ТВиМС;80
4;МОР;85
5;ТВиМС;100

Sample Output:
79
"""

import io
import sys
import pandas as pd

table = sys.stdin.read()
df = pd.read_csv(io.StringIO(table), sep=';')
print(int(df[' grade'].mean()))
