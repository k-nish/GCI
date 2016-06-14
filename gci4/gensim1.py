#coding: UTF-8
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
dictionary.save = ('/var/www/html/gci/gci4/deerwester.dict')
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



