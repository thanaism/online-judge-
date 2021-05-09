# Online Judge

## 環境

Rubyのバージョン管理：`rbenv`
Python：`.venv`に`online-judge-tools`をインストール
Python自体のバージョン管理は`pyenv`

自動テスト：vccodeの`tasks.json`で管理

自分用の勉強メモ

## 剰余の性質

漸化式で表されるような項に対しては剰余の周期性を利用すること（@abc174)
P を法とするような剰余は高々 P 通りしかないということにも着目すること

### 交換法則・結合法則

- $ a \equiv b \Leftrightarrow ac \equiv bc \pmod P $
- $ a \equiv b \Leftrightarrow a+c \equiv b+c \pmod P $
- $ a \equiv b \Leftrightarrow a-c \equiv b-c \pmod P $

### 群と逆元

剰余は群を作る？ため、群論から言えば任意の元に対する逆元が存在する
これについては、まだ必要な問題に当たっていないため後回し

## Python itertools

繰り返しや全列挙系のメソッドがまとまっているライブラリ
実行速度の検証していないが、B 問題くらいまでは超簡潔に記述できそう。

## deque

`deque: double-ended que`
両端からの push, pop に特化したリスト
両端での処理時間が O(1)程度に最適化されている
一方で通常のリストでは先頭 pop などでメモリ移動に O(n)必要となる

## comparison operators

Python では比較演算子は便利なことに連結して書ける

```
# this;
if a<=b and b<=c:
# you can write as below;
if a<=b<=c:
```

## グラフについて

頂点：vertex,node
辺：edge
頂点の集合：$V$
辺の集合：$E$
無向グラフ、有向グラフ

次数が奇数の頂点：奇点
次数が偶数の頂点：偶点

## 一筆書き

### 偶点グラフ

すべてが偶点のグラフなら閉路を取り除いていくと、残ったグラフも必ずすべてが偶点になる
すべてが偶点なら、そのグラフは閉路の集合である

### 奇点グラフ

始点と終点を結ぶ経路を取り除くと残るのは偶点グラフになる

## Euler の多面体定理

木なら：$|V|-|E|=1$
平面上なら：$|V|-|E|+|F|=1$
球面上なら：$|V|-|E|+|F|=2$=>切り開く前はつながっていたので外側も面としてカウント

## 平面グラフに関して

$2E \geqq 3F $

## 完全グラフ

どの 2 つの頂点も 1 本の辺で結ばれているグラフ
完全グラフは$k_n$で表す
グラフ理論の研究者 Kuratowski にちなむ

### 完全グラフの定理

$k_6$の各辺を赤と青の 2 色で彩色しても、赤い辺からなる$k_3$か、青い辺からなる$k_3$が必ず含まれる
拡張するとラムゼー理論

## ホールの結婚定理

すべての女性が知り合いの男性と結婚するのは可能か？
全体のグラフを 2 種類の集合に分け、集合内での辺がないものを 2 部グラフと呼ぶ

### 完全マッチングとは

$V_1$から$V_2$への完全マッチング、というように使う

### ホールの結婚定理の内容

結婚問題に解があるための必要十分条件は、どの$k$人の女性も、合わせて$k$人以上の男性と知り合いであることである

### 無向グラフについて

連結、非連結
閉路
次数
連結で閉路を持たない：木
木は$|E|=|V|-1$
根

### 有向グラフについて

入ってくる辺の集合$\delta_{+}$
出ていく辺の集合$\delta_{ｰ}$
出次数、入次数
有向グラフで閉路を持たない：DAG
DAG: Directed Acyclic Graph
逆向きの辺がないグラフ：トポロジカル順序
トポロジカル順序にする行為：トポロジカルソート

### その他

$|V|$：頂点の個数

### 隣接行列

$|V|\times|V|$の 2 次元配列

| $i/j$ | 0   | 1   | 2   | 3   |
| ----- | --- | --- | --- | --- |
| **0** | 0   | 0   | 0   | 0   |
| **1** | 0   | 0   | 0   | 0   |
| **2** | 0   | 0   | 0   | 0   |
| **3** | 0   | 0   | 0   | 0   |

無向グラフは双方性あるが、有向グラフでは双方性がない
重み付きグラフなら 01 ではなく重みを記入する

関係性の取得は O(1)だが、管理に O(|$V^2$|)のコストがかかる。

### 隣接リスト

頂点ごとに隣接する頂点のリスト情報を持つ

| $V$ | list |
| --- | ---- |
| 0   | 1,3  |
| 1   | 0,2  |
| 2   | 1    |

可変長配列でないとこれもメモリを圧迫する

## グリッドが与えられた際のグラフへの変換

とりあえず、$iW+j$につぶしてしまうというのも手
ワーシャルフロイド法では、隣接行列が必須

### 隣接リスト

基本的にはこっちが使われることがほとんどである
可変長配列でないと空間計算量が$O(VE)$になってしまう（意味はよくわからん）

## FILO: First In Last Out

これがキュー

## FIFO: First In First Out

これがスタック

## Python 自体の言語仕様

### set

集合演算には非常に強力である。

```Python
# {}で囲うことでsetとなる
a = {1,2,3,4}

# リストをset化する場合
a = set([1,2,3,4])

# タプルをset化する場合
a = set((1,2,3,4))
```

和、積、差、対称差を取ることが可能。

#### union

```python
>>> a | b
>>> a.union(b)  # aを維持
>>> a.update(b)  # a自体を拡張
```

#### intersection

```python
>>> a & b
>>> a.intersection(b)  # aを維持
>>> a.intersection_update(b)  # a自体を拡張
```

#### difference

```python
>>> a - b
>>> a.difference(b)  # aを維持
>>> a.difference_update(b)  # a自体を拡張
```

#### symmetric difference

```python
>>> a ^ b
>>> a.symmetric_difference(b)  # aを維持
>>> a.symmetric_difference_update(b)  # a自体を拡張
```

#### subset

```python
>>> a <= b
>>> a.issubset(b)
```

#### superset

```python
>>> a => b
>>> a.issuperset(b)
```

#### disjoint

```python
>>> a.isdisjoint(b)
```

#### frozenset

```python
>>> a = frozenset((1,2,3,4))
# a is immutable
```

#### methods

```python
len(a)
a.add(b)
a.discard(b)
a.remove(b)  # b must be in set b
a.pop(b)
a.clear()
```

### .index()
対象の配列から、一致する最初のインデックスを取り出す。
2番目以降を取得したい場合は、第2引数に指定する。


