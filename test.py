from gensim.models import word2vec
from gensim import models
import logging
from gensim.models import KeyedVectors

# Total accuracy: 24.8%
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#讀取model
print("Load Model...")
model = models.Word2Vec.load('wiki.zh.text.model')
print("Load OK")
word_vectors = model.wv
print("mode2vec OK")
# word_vectors.save("cbow.vector")
# Load back with memory-mapping = read-only, shared across processes.
print("Load Vector...")
# wv = KeyedVectors.load("cbow.vector", mmap='r')
print("Load OK")
#詞相似度分析
#similarities = model.wv.evaluate_word_pairs('MEN.txt')  #繁體中文
#similarities = model.wv.evaluate_word_pairs('simlex999.txt')
# similarities = model.wv.evaluate_word_pairs('wordsim-240.txt')      #簡體中文
similarities = model.wv.evaluate_word_pairs('trd-wordsim-240.txt')  #繁體中文
print("ws240評估完成")
#similarities = model.wv.evaluate_word_pairs('wordsim353.tsv')
similarities = model.wv.evaluate_word_pairs('trd-wordsim-297.txt')  #繁體中文
print("ws296評估完成")
# similarities = model.wv.evaluate_word_pairs('wordsim-297.txt')      #簡體中文
# print(similarities)
similarities = model.wv.evaluate_word_pairs('zh_tw_ws353.txt')  #繁體中文
print("ws353評估完成")
similarities = model.wv.evaluate_word_pairs('zh_tw_ws353_relatedness.txt')  #繁體中文
print("ws353-relatedness 評估完成")
similarities = model.wv.evaluate_word_pairs('zh_tw_ws353_similarity.txt')  #繁體中文
print("ws353-similarity評估完成")
similarities = model.wv.evaluate_word_pairs('zh_tw_SimLex-999.txt')  #繁體中文
print("simlex-999評估完成")
similarities = model.wv.evaluate_word_pairs('zh_tw_bruni_men.txt')  #繁體中文
print("MEN評估完成")
similarities = model.wv.evaluate_word_pairs('zh_tw_radinsky_mturk.txt')  #繁體中文
print("Mturk評估完成")
analogy_scores = model.wv.evaluate_word_analogies('zh_tw_google.txt')  #繁體中文
#詞類比分析
print("CKIP詞類比評估完成")
analogy_scores = model.wv.evaluate_word_analogies('analog.txt')  #繁體中文
# analogy_scores = model.wv.evaluate_word_analogies('analogy.txt') #簡體中文
# analogy_scores = model.wv.evaluate_word_analogies('questions-words.txt')
# print(analogy_scores)
#122/848
#2057/7817
print("模型評估完成")

from gensim.test.utils import 
from gensim.models import word2vec
from gensim import models
import logging
from gensim.models import KeyedVectors

# Total accuracy: 24.8%
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#讀取model
print("Load Model...")
model = models.Word2Vec.load('wiki.zh.text.model')
print("Load OK")
word_vectors = model.wv
print("mode2vec OK")
# word_vectors.save("cbow.vector")
# Load back with memory-mapping = read-only, shared across processes.
print("Load Vector...")
# wv = KeyedVectors.load("cbow.vector", mmap='r')
print("Load OK")
#詞相似度分析
#similarities = model.wv.evaluate_word_pairs(('MEN.txt')  #繁體中文
#similarities = model.wv.evaluate_word_pairs(('simlex999.txt')
# similarities = model.wv.evaluate_word_pairs(('wordsim-240.txt')      #簡體中文
similarities = model.wv.evaluate_word_pairs(('trd-wordsim-240.txt')  #繁體中文
print("ws240評估完成")
#similarities = model.wv.evaluate_word_pairs(('wordsim353.tsv')
similarities = model.wv.evaluate_word_pairs(('trd-wordsim-297.txt')  #繁體中文
print("ws296評估完成")
# similarities = model.wv.evaluate_word_pairs(('wordsim-297.txt')      #簡體中文
# print(similarities)
similarities = model.wv.evaluate_word_pairs(('zh_tw_ws353.txt')  #繁體中文
print("ws353評估完成")
similarities = model.wv.evaluate_word_pairs(('zh_tw_ws353_relatedness.txt')  #繁體中文
print("ws353-relatedness 評估完成")
similarities = model.wv.evaluate_word_pairs(('zh_tw_ws353_similarity.txt')  #繁體中文
print("ws353-similarity評估完成")
similarities = model.wv.evaluate_word_pairs(('zh_tw_SimLex-999.txt')  #繁體中文
print("simlex-999評估完成")
similarities = model.wv.evaluate_word_pairs(('zh_tw_bruni_men.txt')  #繁體中文
print("MEN評估完成")
similarities = model.wv.evaluate_word_pairs(('zh_tw_radinsky_mturk.txt')  #繁體中文
print("Mturk評估完成")
analogy_scores = model.wv.evaluate_word_analogies(('zh_tw_google.txt')  #繁體中文
#詞類比分析
print("CKIP詞類比評估完成")
analogy_scores = model.wv.evaluate_word_analogies(('analog.txt')  #繁體中文
# analogy_scores = model.wv.evaluate_word_analogies(('analogy.txt') #簡體中文
# analogy_scores = model.wv.evaluate_word_analogies(('questions-words.txt')
# print(analogy_scores)
#122/848
#2057/7817
print("模型評估完成")

