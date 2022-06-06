# 概要

二分探索のコードをPythonで書いてみます。あわせて、コードを書き上げるまでにどのようなことを考えていくか追っていきます。

## ゴール

二分探索とは何か・どのように問題を分解し、考えていくことでコードを組み立てられるのか理解することを目指します。

## 目次

[toc]

## 復習-探索処理を考えるときの大まかな流れ

最初に、探索処理をコードで表現するときの基本的な流れを復讐しておきます。
やりたいことをざっくり書き出すと、

* リスト、あるいは配列を探索範囲として用意
* 探索対象(数値)・探索開始地点(リスト/配列内の一要素)を決定
* 現在参照している要素が探索対象と一致するか判定
* 一致しない場合は、次の要素を参照
* 探索対象が見つかるか、探索の終了条件を満たすまで探索を続行

といったようになります。
コードで見た方がより明確なイメージが掴めるかと思いますので、線形探索を例に見てみましょう。

```Python
# 線形探索
def search(search_list: list[int], target: int) -> Union[int, None]:

    for index, item in enumerate(search_list):
        if item == target:
            return index

    return None
```

引数で探索範囲と対象を決めています。そして、ループ処理の部分が探索の要となる、探索対象が範囲に存在するか探し回っているところです。
二分探索では、ループで書かれている処理のロジックが二分探索を表現したものへと置き換わります。
言い換えれば、二分探索を考えるということは、`どのように次の要素を参照していくのか`・`どんな条件を満たすと探索が終了するのか`を明確にすることだと言えます。

更新処理・終了条件をどのように組み立てていくのか、じっくりと見ていきます。


## 二分探索とは

二分探索とは、探す対象となるリストを半分・更に半分と、2つに分けることを繰り返しながら探索していくアルゴリズムです。
[参考](https://en.wikipedia.org/wiki/Binary_search_algorithm)

### アルゴリズムを分解してみる

線形探索と比べると、一気に難しくなりました。2つに分けるということだけではコードを書くのも難しそうなので、アルゴリズムを小さな要素に分けて考えてみます。もう少し詳しく言語化できれば、アルゴリズムのイメージも固まるはずです。

#### 半分に分ける

半分に分ける、という動作は日常でも馴染み深いものなので、リストを2等分することもなんとなくイメージできるかもしれません。
しかし、コードでこのような操作を表現するには、半分に分ける位置、すなわち`中央`をどのように決めるか明確にしなければなりません。

#### 探す方向

まず、二分探索アルゴリズムは、探索対象となるリストがソート済みであることが前提です。また、話を簡単にするため、今回は固定で昇順であるものを扱うことにします。
ソート済みであれば、探すリストを半分に分けたとき、リストが中央を基準に、探したいものより大きいもの・小さいものへと分かれます。すると、探したいものに応じて、前方(大きい方)・後方(小さい方)と探しに行く方向が変わります。

```Python
# 探索対象リスト
# 要素「3」を中央として分割すると、前方には3より大きいもの・後方には3より小さいものだけが残る
sorted_search_list = [1, 2, 3, 4, 5]
# 以下のように探索対象が小さくなることで、問題を小さく扱いやすくすることができる
# 前方
former = [4, 5]
# 後方
latter = [1, 2]
```

双方向をまとめて考えると混乱しそうなので、前方の二分探索・後方の二分探索と分けて見ていくことにします。こうすることで、二分探索の完成形に表れる複雑な分岐も理解できるようになるはずです。


---

さて、二分探索アルゴリズムでやるべきことを少し細かく見てきました。これを振り返って、二分探索をコードで記述する上で考える手順を整理してみましょう。

* 中央とはどこか明確にする
* 前方/後方それぞれの二分探索を別々に考える
* 最後に双方向の探索を組み合わせ、二分探索を完成させる

このように問題を分解してみると、なんとか立ち向かえそうです。以降では小さく分けた問題を1つずつ見ていきます。

## 中央を知る

ここでは、中央がどのようなものか明らかにします。人目では直感的に分かる概念ですが、コンピュータに中央を理解させなければ、二分探索アルゴリズムを実装することはできません。
中央とはなんぞやまで深掘りするのはやめておき、ここでは、とりあえず、`2つの要素があるとき、要素間の中央はそれぞれの要素との距離が等しい`と捉えることにします。
`[1, 2, 3, 4, 5]`のようなリストを例にしてみます。このようなリストの中央はどこなのでしょうか。

直感的には、2番目の要素である`3`がリストの中央であるように見えます。 リストの要素同士の距離は、添え字の差から求めることができそうです。
例えば、0番目の要素と1番目の要素の距離は、`1 - 0 = 1`・2番目の要素と5番目の要素の距離は、`5 - 2 = 3`といった具合です。
ということは、中央は配列の先頭と末尾との添え字の差、すなわち距離が等しいものを探せば良さそうです。

先ほど、なんとなくで決めた2番目の要素で考えてみると、先頭は、`2 - 0 = 2`・末尾は`4 - 2 = 2`で先頭と末尾からの距離が同じとなりました。
リストの先頭・末尾における中央は、それぞれとの距離が等しい2番目の要素であることを計算で導き出せるようになりました。

---

これで、中央を算出する方法が見えてきました。今度は、コードでどのように中央を求めるか見てみましょう。

### コードで中央を書いてみる

先ほどまで見てきた例をコードで表してみます。リストとその先頭・末尾の添字を定義し、中央の位置を計算しています。

```Python
import math

# 探索対象リスト
sorted_search_list = [1, 2, 3, 4, 5]
# 先頭・末尾の添字
head = 0
tail = len(sorted_search_list) - 1

# 中央の位置を算出
mid = math.floor((head + tail) / 2)
```

リストを定義し、先頭・末尾の添字をそれぞれ`head・tail`と表現しています。中央は、先頭・末尾の添字をもとに導き出すことができます。コード上では小数部分を切り上げていますが、これは添字としてアクセスできるようにするためなので、切り捨てでも問題はありません。
また、足して2で割る操作がしっくりこない場合は、座標の中点を求める方法を考えてみると理解の助けとなるかもしれません。

---

これで中央を求める、つまり二分探索でリストを半分に分ける操作をコードで表せるようになりました。あとは、リストを前方/後方に進んでいく操作を表現できるようになれば、二分探索ができあがります。
それぞれ順にコードへと落とし込んでいきます。

#### 補足: 中央の求め方(別パターン)

二分探索で中央を求める処理は、これまで見てきた式でなく`head + (tail - head) / 2`のように表現しているものを見かけるかもしれません。
一見すると別の求め方をしているように見えますが、左側の`head`を`2 * head / 2`と置き換えれば、これまで見てきた式と同じ形になります。それでは、なぜ別の表現で書くことがあるのでしょうか。

これは、先頭と末尾の添字を足した結果がリストの添字を表現する数値型の最大値を超えないようにするためです。
`head + (tail - head) / 2`は末尾の添字`tail`より大きくなることはありません。しかし、`(head + tail) / 2`は、計算の途中で`tail`よりも大きくなります。例えば添字が4バイトの数値型であれば、`head + tail`が数十億を超えると、問題となってしまいます。

やや細かい話となってしまったので、ひとまずここでは計算過程にて扱う数値が大きくなりすぎないよう、式の形を変えることもあるんだな、ということを覚えておきましょう。

[参考](https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2#%E5%AE%9F%E8%A3%85%E4%B8%8A%E3%81%AE%E9%96%93%E9%81%95%E3%81%84)

## 前方のみ探索

前方は、リストの右側、つまり添え字がより大きくなる方向を指します。
つまり、線形探索とは進む方向が同一で、進む大きさのみが異なる二分探索を考えてみます。いきなり条件によって前に進んだり、後ろに進んだりされると、頭が混乱してしまうので、まずはシンプルに前に進み続けます。

ここでは、前方にだけ進む二分探索がより具体的にどのようにリストを進んでいくのか・どのような条件を満たすと探索が終了するのか明らかにします。

### 進み方

二分探索がどのように前へと動いていくのか探ってみます。線形探索も前方へと進んでいきますが、進み方を言い換えると、添字を1つずつ増やすように前方へと動いていました。
二分探索はどのように添字を変えながら前方へと動いていくのでしょうか。

一言で表すと、リストを中央で半分に分けたときの前方のみを残しながら進んでいきます。比較するために線形探索も同じように考えると、リストを先頭から1つずつ除いたものを残しながら進んでいきます。
10個の要素があるリストで実際に進みながら見てみてましょう。

```Python
# 探索範囲 中央は要素「6」
# 要素「6」より前方が次の探索範囲となる
search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# 探索範囲 中央は要素「9」
# 要素「9」より前方が次の探索範囲となる
former_1st = [7, 8, 9, 10, 11]
# 探索範囲 中央は要素「11」
# 要素「11」より前方は存在しないので打ち切り
former_2nd = [10, 11]
```

リストの中央を決め、中央より前方にあるものを探索範囲として置き換えています。
より具体的には、1回目の探索では10個の要素すべてが範囲・2回目では中央の要素「6」より前方の5個の要素が範囲・3回目で中央の要素「9」より大きい2個の要素が範囲となります。
このようにリストを走査していくことで、線形に1つ1つ調べるよりも、効率よく調べることができます。

#### 更新処理

コード上でどのようにリストの前方のみを残すのか、イメージを固めておきます。
中央の位置は計算で求められるようになったので、リストの添え字の形で参照できます。これを1つ進めたものが先頭・元のリストの末尾をそのまま末尾としてリストを作り替えれば、中央よりも先の要素だけを残したものがつくれそうです。
サンプルコードでも見てみましょう。

```Python
search_list = [1, 2, 3, 4, 5]
# 中央の位置
mid_index = 2
# 中央の位置+1番目が先頭となるように分けていけば、中央より前方だけが残る
former_1st = search_list[mid_index+1:]
# [4, 5]
```

このように前方へと進んでいくたびに先頭を動かしていけば、探索範囲のリストをどんどん小さくしていけそうです。

### 終了条件

続いて、いつ探索を終えるのか考えてみます。
線形探索ではすべての要素を走査し終えたとき、という明確な区切りがありました。ですが、二分探索はリストを半分ずつに分けながら進んでいくので、一見しただけではいつ終わるのかが見えづらそうです。
こういうときは小さなリストから順々に追っていくと見えやすくなります。コードで具体的に見てみましょう。

```Python
# 要素数1
search_list = [1]
# 0番目
mid_index = math.floor((0 + 0) / 2)
# 中央より前方はこれ以上存在しないので、打ち切り

# 要素数2
search_list = [1, 2]
# 1番目
mid_index = math.floor((0 + 1) / 2)
# 中央より前方はこれ以上存在しないので、打ち切り

# 要素数3
search_list = [1, 2, 3]
# 1番目
mid_index = math.floor((0 + 2) / 2)
# 1番目より前方は2番目の要素しかないので、要素数1のときと同じ状態になる
```

どうやら、中央より前にある要素が無くなったときにこれ以上探索できなくなるようです。中央を求める操作が切り捨てであった場合も、同じ結果となります。
しかし、リストを中央の位置+1番目の要素が先頭になるように分けていくと、これ以上分けられなくなったときに予期しない動きをしそうです。

```Python
search_list = [1]
# 0番目
mid_index = math.floor((0 + 0) / 2)
# 1番目の要素は存在しないのでサブリストがつくれない
sub_list = search_list[mid_index+1:]
```

ここで、小さくなったリストの実体を毎回つくっていては効率が悪いので、リストの先頭・末尾の添字を表現する変数を動かすことでリストを小さくしていきます。

```Python
# 初期状態
# headが先頭・tailが末尾のリストは、探索範囲のリスト全体を指す
head = 0
tail = 4
search_list = [1, 2, 3, 4, 5]
# 中央の位置
mid_index = 2
# 中央をもとに先頭を更新
# すると、headが先頭・tailが末尾のリストは、中央より前方のみが残る
head = mid_index + 1
```

添字の参照を動かすことでリストを小さくしていけば、

```Python
head = 0
tail = 0
search_list = [1]
# 0番目
mid_index = math.floor((0 + 0) / 2)
# 1となり、リストの範囲外となる
head = mid_index + 1
# 末尾の添字はつねにリストの終端を指しているので、
```


### 実装


```Python
# binary_search/binary_search.py

def search_forward(search_list: list[int], target: int) -> Union[int, None]:
    """
    前方のみの二分探索

    :param search_list: 探索対象リスト
    :param target: 探索対象
    :return: 合致するものがリストに存在 -> 探索対象のリスト内インデックス, 存在しない -> None
    """

    sorted_search_list = sorted(search_list)

    # 先頭・末尾 初期値はリストの先頭・末尾と対応
    head = 0
    tail = len(sorted_search_list) - 1

    while head <= tail:
        # 中央の位置を算出
        mid = math.floor((head + tail) / 2)

        if sorted_search_list[mid] == target:
            return mid

        # 先頭を更新することで探索範囲を狭める
        head = mid + 1

    # 合致なし
    return None
```


## 後方のみ探索

## 二分探索


## まとめ