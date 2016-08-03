import re

import networkx as nx
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

def get_highest_pagerank_scores(artifact, n=5):

#        text = 
        sentences = re.findall(r'.*?\n', text, flags=re.DOTALL)

    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(sentences)
    
    transformer = TfidfTransformer()
    normalized = transformer.fit_transform(matrix)
    
    similarity_graph = normalized * normalized.T
    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    
    scores = nx.pagerank(nx_graph)
    
    index_scores = scores.items()
    sorted_scores = sorted(index_scores, key=lambda x: x[1], reverse=True)
    
    for index, score in sorted_scores[:n]:
        print(score, sentences[index])
