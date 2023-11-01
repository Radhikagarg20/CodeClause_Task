import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_score
# import spacy

user_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
user_notes = [open(_file, encoding='utf-8').read()
                 for _file in user_files]

# nlp = spacy.load('en_core_web_sm')

user_files = ['text1', 'text2', 'text3', 'text4']

user_notes = ['As saying goes, The lazy dog jumped over by the quick brown fox.',
 'The quick brown fox leaps over the lazy canine.',
 'The quick brown fox jumps over the lazy dog.',
 'The quick brown fox jumps over the lazy dog, as the saying goes.']

def vectorize(Text):
    return TfidfVectorizer().fit_transform(Text).toarray()

def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

vectors = []
# for note in user_notes:
#     doc = nlp(note)
#     vectors.append(doc.vector)
    
vectors = vectorize(user_notes)
s_vectors = list(zip(user_files, vectors))
plagiarism_results = set()

# s_vectors

def check_plagiarism(s_vectors):
    for text_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((text_a, text_vector_a))
        del new_vectors[current_index]
        for text_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((text_a, text_b))
            score = (student_pair[0], student_pair[1], sim_score)
            plagiarism_results.add(score)
    return plagiarism_results

threshold = 0.75

print(check_plagiarism(s_vectors))