#coding: UTF-8
# gensim tutorial:corpora and vector spaces
import logging
# ログ活動を見たいときはlogginをimportして以下のコードが必要
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
documents = ["Human machine interface for lab abc computer applications", "A survey of user opinion of computer system response time","The EPS user interface management system","System and human system engineering testing of EPS","Relation of user perceived response time to error measurement","The generation of random binary unordered trees","The intersection graph of paths in trees","Graph minors IV Widths of trees and well quasi ordering","Graph minors A survey"]
# common wordsを取り除き、トークン化(単語分割)
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

# 一度しか出現しない単語を取り除く
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
	for token in text:
		frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]

from pprint import pprint
print('texts')
pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('/var/www/html/gci/gci4/deerwester.dict')
print('dictionary')
print(dictionary)

# 12個の単語(token)をdictionaryに追加し、出現度から12個のベクトルとして各単語にidを振り分ける。tokenとidを表示するのがtoken2id
print('dictionary.token2id')
print(dictionary.token2id)

# 新しいドキュメントをベクトルにしてみる
# doc2bowは各単語の出現回数を数え、idとともにスパースベクトルとして返す(id,出現回数)
new_doc = 'Human computer interaction'
new_vec = dictionary.doc2bow(new_doc.lower().split())
print('new_vec')
print (new_vec)

# 各単語をドキュメント全体の中の出現率からidで分類し、スパース行列によって各単語を書き換えたドキュメントを出力
corpus = [dictionary.doc2bow(text) for text in texts]
# ディスクに保存する処理
corpora.MmCorpus.serialize('/var/www/html/gci/gci4/deerwester.mm', corpus)
print 'corpus'
print(corpus)

# corpusはpythonのリストとして保存される。上の例だとcorpusはメモリに保存されているがcorpusのデータ量が大きくなるとメモリには保存できなくなる。ここでディスク上にcorpusが保存されているとする。さらにcorpusは各単語がスペースで区切られているとする。
class MyCorpus(object):
	def __iter__(self):
		for line in open('mycorpus.txt'):
			# assume there's one document per line, tokens separated by whitespace
			yield dictionary.doc2bow(line.lower().split())

corpus_memory_friendly = MyCorpus()
print corpus_memory_friendly

# corpusの中身を可視化するためにはcorpus_memory_friendlyを一列ずつ表示しなくてはならない
for vector in corpus_memory_friendly:
	print (vector)

# すべてのテキストをメモリに読むことなく辞書を作成するコードを記述する
# すべてのトークンに関するデータを読み込む
dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))
# 最後の言葉、一度しか登場しない単語を消去する
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) #最後の言葉、一言しか登場しない単語を消去
dictionary.compactify() #取り除かれた単語のidも取り除く
print 'dictionary'
print dictionary

# 辞書のファイル形式にもいろいろなものがある。ここでは、Market Matrix Formatという有名なファイル形式で保存する方法をあげる
from gensim import corpora
# まずは単なるPythonのリストとして2単語の辞書を作る
corpus = [[(1, 0.5)], []] #ここではなんとなく片方の単語を空にする
corpora.MmCorpus.serialize('/var/www/html/gci/gci4/corpus.mm', corpus)

# 他の有名なファイル形式Joachim's SVMlight format, Blei's LDA-C format, GibbsLDA++formatへの保存方法は
# corpora.SvmLightCorpus.serialize('/var/www/html/gci/gci4/corpus.svmlight', corpus)
# corpora.BleiCorpus.serialize('/var/www/html/gci/gci4/corpus.lda-c', corpus)
# corpora.LowCorpus.serialize('/var/www/html/gci/gci4/corpus.low', corpus)

# 逆に.mmファイルを読み込むコードは
corpus = corpora.MmCorpus('/var/www/html/gci/gci4/corpus.mm')

# 辞書の中身を出力する方法 print(corpus)では入っているデータの情報しか出力されず何が入っているかわからない
# まず1つの方法が
print 'list(corpus)'
print list(corpus)
# もう一つの方法が
for doc in corpus:
	print(doc)

# Matrix Market document形式の辞書をBlei's LDA-C formatに保存する形式は
# corpora.BleiCorpus.serialize('var/www/html/gci/gci4/corpus2.lda-c', corpus)

# gensimにはnumpy matrixと互換性をもつ機能を持っている
# import gensim
# corpus = gensim.matutils.Dense2Corpus(numpy_matrix)
# numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=number_of_corpus_features)
# scipy matrixとの互換するコード
# corpus = gensim.matutils.Sparse2Corpus(scipy_sparce_matrix)
# scipy_csc_matrix = gensim.matutils.corpus2csc(corpus)






