import sys

def calc1(s: str) -> float:
  """
  文字列を数値に変換する。
  s: str
    変換対象の数値文字列
  """
  return float(s)

def calc2(s: str) -> float:
  """
  2項の加算を計算する。
  s: str
    処理対象の加算式文字列
  """
  # 演算子の位置を特定
  pos = s.find('+') # "1+2 なら 1"
  if pos > 0:
    left = s[:pos]
    right = s[pos + 1:]
    return float(left) + float(right)

if __name__ == '__main__':
  args = sys.argv
  #result = calc1(args[1])
  result = calc2(args[1])

  print(result)
