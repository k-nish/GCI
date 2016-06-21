# coding: UTF-8
# gensim tutorial:topis and transformations
# ログを取るために必要な処理
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/var/www/html/gci/gci4/deerwester.dict')
corpus = corpora.MmCorpus('/var/www/html/gci/gci4/deerwester.mm')
print "corpus"
print corpus
# 以下一次ベクトルで表現されたドキュメントを別の表現に変換する処理を行う。この処理の目標は2つある。
# 1.corpus内の隠された関係性、単語同士の関係性を見つけ、新しい、可読性のある方法でドキュメントを説明する
# 2.より必要なリソースを減らす、余分な情報を減らすという2点においてドキュメントをよりコンパクトにする

# モデルを初期化する
tfidf = models.TfidfModel(corpus)
# tfidfでは与えられたcorpusをトレーニングセットとして利用してドキュメントないの単語の情報を取得することで分析を行う。
# 異なる表現変化では別のデータセットを利用するべきであり、LSA,LDAではより発展し、時間のかかる処理が必要になる

# tfidfではbag-of-words(出現率のみのデータ)形式の表現から新しい表現(tfidfによる重みがつけられた表現)に変換する
doc_bow = [(0,1),(1,1)]
# モデルを用いてベクトルに変換する
print tfidf[doc_bow]
# モデルを用いてcorpus全体に適用する
corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
	print doc
# この例ではトレーニングで用いたcorpusと全く同じものを変形に用いている。これは特殊な例であり、変形で用いるモデルは一度初期化されれば同じスパース行列も含めてどんな行列でもよい。
# model[corpus]はドキュメントの反復中のみ変換されているのであって、記憶ディスク内のデータが変換されているわけではない。従って、変形された行列を何度も使いたいときはcorpora.MmCorpus.selialize(保存先のパス, corpus)でディスク内にserializeする必要がある

# tfidfコーパスをlatent semantic indexingを用いてlatent 2D空間に変形する(num_topicsの数字が変形先の次元)
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2) #LSI変形の初期化
corpus_lsi = lsi[corpus_tfidf]
# 特徴量を出力する
print 'lsi.print'
lsi.print_topics(2)
# output
# topic #0(1.594): 0.703*"trees" + 0.538*"graph" + 0.402*"minors" + 0.187*"survey" + 0.061*"system" + 0.060*"time" + 0.060*"response" + 0.058*"user" + 0.049*"computer" + 0.035*"interface"
# topic #1(1.476): 0.460*"system" + 0.373*"user" + 0.332*"eps" + 0.328*"interface" + 0.320*"time" + 0.320*"response" + 0.293*"computer" + 0.280*"human" + 0.171*"survey" + -0.161*"trees"
# これより、trees,graph,minorsが全て関連性のある単語であることがわかり、(firstトピックの方向に寄与している)その一方で二番目のトピックは他全ての単語を扱っている。

# 各ドキュメントの2つのトピックとの関連度を出力
# 予想される通り、最初の5つのドキュメントは2つめのトピックに強く関連していて、残りの4つのドキュメントは1つめのトピックに関連している
for doc in corpus_lsi:
	print doc

# 他の処理のためモデルを保存したいときは以下の処理を行う
lsi.save('/var/www/html/gci/gci4/model.lsi')
lsi = models.LsiModel.load('/var/www/html/gci/gci4/model.lsi')

# これらのドキュメントが以下に関連性のあるものなのかを示す方法を考える。類似性を一般化する方法を考える
# Tf-idf(Term Frequency Inverse Document Frequency)は出現数を表す整数値のベクトルを用いて類似性を示す実数値からなるベクトルに変形する
model = tfidfmodel.TfidfModel(bow_corpus, normalize=True)

# LSI(Latent Semantic Indexing)は出現数を表す整数値からなるベクトルとtfidfによる重みつけされた単語のベクトルを用いて変形を行う。上の例では2次元でしか扱わなかったが実際のcorporaでは目標となる次元は200から500が黄金律とされている
model = lsimodel.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=300)
# LSIによる学習の特徴は学習中のいつでも新たな学習ドキュメントを追加することによって学習を続けられることにある。この特徴によってモデルに入力されるドキュメントは無限になり、ドキュメントが入力されるたびに計算済みの変形モデルを使いながらLSIのモデルを学習させ続けることができる。
model.add_documents(another_tfidf_corpus) #LSIに既存のコーパスに加えて新しいコーパスを学習させる
lsi_vec=model[tfidf_vec] #新しいドキュメントをLSI空間に変形させることができる
# この2行のコードを繰り返すことで無限に学習させることができる

# RP(Random Projections)はベクトル空間の次元を減らすことを目標としている。RPはメモリ,CPUの両方にとって効率的にtfidfの距離を概算することができる。誤差はデータセットのサイズに依存する
model = rpmodel.RpModel(tfidf_corpus, num_topics=500)

# LDA(Latent Distance Allocation)は出現数を表す整数値のベクトルからより次元の低いトピック空間に変換するための変形処理である。LDAはLSAを確率モデルを用いて拡張したものであり、LDAのトピックは単語の確率分布として解釈される
model = ldamodel.LdaModel(bow_corpus, id2word=dictionary, num_topics=100)

# HDP(Hierarchical Dirichler Process)はノンパラメトリックのベイズ手法である
model = hdpmodel.HdpModel(bow_corpus, id2word=dictionary)























