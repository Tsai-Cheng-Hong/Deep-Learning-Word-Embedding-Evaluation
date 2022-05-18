# Deep-Learning-Word-Embedding-Evaluation
使用詞相似度(Word Similarity)與詞類比(Word Analogy)評估詞嵌入模型訓練出來的詞向量

如果是使用gensim套件訓練出來的模型，如CBOW、Skipgram、FastText等

請使用test.py進行模型的評估，參考test.ipynb。

如果是使用C語言訓練出來的模型，如CWE、JWE、...等

請使用word_sim.py與word_analogy.py進行模型的評估，可以參考Evalate_Model.ipynb

# Word Analogy
analog.txt為繁體Dataset，將analogy.txt使用OpenCC翻譯得到。

analogy.txt為簡體Dataset，由[1]提供。

zh_tw_google.txt為繁體Dataset，由[2][3]提供。

# Word Similarity

trd-wordsim-240.txt為繁體Dataset，由[2][3]提供。

trd-wordsim-297.txt為繁體Dataset，由[2][3]提供。

wordsim-240.txt為簡體Dataset，由[1]提供。

wordsim-297.txt為簡體Dataset，由[1]提供。

zh_tw_SimLex-999.txt為繁體Dataset，由[2][3]提供。

zh_tw_bruni_men.txt為繁體Dataset，由[2][3]提供。

zh_tw_radinsky_mturk.txt為繁體Dataset，由[2][3]提供。

zh_tw_ws353.txt為繁體Dataset，由[2][3]提供。

zh_tw_ws353_relatedness.txt為繁體Dataset，由[2][3]提供。

zh_tw_ws353_similarity.txt為繁體Dataset，由[2][3]提供。

# 已經訓練好的詞向量
已經訓練好的詞向量下載:https://github.com/Tsai-Cheng-Hong/Deep-Learning-Word-Embedding

# Reference:
[1] P. Jin and Y. Wu, "Semeval-2012 task 4: evaluating chinese word similarity," in * SEM 2012: The First Joint Conference on Lexical and Computational Semantics–Volume 1: Proceedings of the main conference and the shared task, and Volume 2: Proceedings of the Sixth International Workshop on Semantic Evaluation (SemEval 2012), 2012, pp. 374-377. 

[2] C.-Y. Chen and W.-Y. Ma, "Word embedding evaluation datasets and wikipedia title embedding for Chinese," in Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018), 2018. 

[3] C.-Y. Chen and W.-Y. Ma, "Embedding wikipedia title based on its wikipedia text and categories," in 2017 International Conference on Asian Language Processing (IALP), 2017: IEEE, pp. 146-149. 
