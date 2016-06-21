# coding: UTF-8
# gensim tutorial similarity queries

# ログを取るために必要な処理
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

# gensim1.py,gensim2.pyと同様にコーパスを設定する
from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/var/www/html/gci/gci4/deerwester.dict')
corpus = corpora.MmCorpus('/var/www/html/gci/gci4/deerwester.mm')
print 'corpus'
print corpus

# 2次元のLSI空間を用いてDeerWesterの例を見る
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

# "Human computer interaction"という入力に対して関連度の昇順にコーパス内の9つの文章を並べ替える。
doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]
print vec_lsi
# 2つのベクトルの類似性を測るためにはcosを用いる。ベクトル空間のモデリングではcosを用いた類似性の測定が主流だが、他の手法が最適となる

# 検索語の類似性測定のために比較するための全ての文書を用意する必要がある。下の例ではトレーニングLSIも、変換される2次元のLSA空間も同じものを使っているが実際は全く異なるコーパスを用いてよい。
index = similarities.MatrixSimilarity(lsi[corpus]) #コーパスをLSI空間に変換
# 注意:百万のコーパスに対してsimilarities.MatrixSimilarity()を用いる場合2GBのフリーなメモリが必要になる。2GB以上の空きメモリがない場合にはsimilarities.Similarities classを使う必要がある。

# LSI空間に変換されたindexを保存、もしくは読み込むときのコード
index.save('/var/www/html/gci/gci4/deerwester.index')
index = similarities.MatrixSimilarity.load('/var/www/html/gci/gci4/deerwester.index')
# index形式を扱うのはsimilarities.Similarity,similarities.MatrixSimilarity,similarities.SparseMatrixSimilarityの3つのクラスがあるがどのクラスを用いて扱えばいいかわからないときはsimilarities.Similarityを使えばよい。これがもっとも拡張性があり、indexにより多くの文書を追加することにも対応しているからである。

# 9つのindexにされた文書に対する検索語の類似性を出力する
sims = index[vec_lsi] #コーパスに対する検索語を測る
print list(enumerate(sims)) #ドキュメントの番号とドキュメントとの類似性を2次元のタプルで表現する

# cosは-1から1までの値を取り、より大きい値をとるときその文書と検索語の類似性が高いと言える。
# 検索語と関連度が高い順にタプルを並び替える
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sims





