## メモ
* 字句解析⇒構文解析
  - 構文木
  - 自然言語⇒曖昧(複数の解釈)
    - 人工言語⇒曖昧さを排除(パターンから構文木の構造を決定)

## コマンド
* [コマンドラインから実行関数を指定](https://qiita.com/kenichi-hamaguchi/items/dda5532f3b218142e7c9)
### 汎用的なmain関数を作る
```python
import argparse
if __name__ == '__main__':
  # -- オプション追加 --
  parser = argparse.ArgumentParser()
  # オプション追加 - 関数名
  parser.add_argument(
    'function_name',
    type = str
  )
  # オプション追加 - 関数の引数
  parser.add_argument(
    '-i',
    '--func_args',
    nargs = '*',
    default = []
  )
  # -- コマンドライン引数から関数を特定して実行 --
  # ファイル内の関数を取得
  func_dict = {k: v for k in locals().items() if callable(v)}
  # 引数のうち、数値として解釈できる要素はfloatにcastする
  func_args = [float(x) if x.isnumeric() else x for x in args.func_args]
  # 関数実行
  ret = func_dict[args.function_name](*func_args)
```
#### 実行
`python <file.py> <関数名> -i <関数内引数>`