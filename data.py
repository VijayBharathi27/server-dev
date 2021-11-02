# this file is used for testing the removing duplicates algorithm seperately

import spacy
import en_core_web_lg


nlp = en_core_web_lg.load()


def check_concat(a, b, index_a):
    clone = 0
    job_a = a[index_a]
    for index_b in range(0, len(b)):
        job_b = b[index_b]
        comp_a = job_a.get('employer')
        comp_a = ' '.join(comp_a.lower().split())
        comp_b = job_b.get('employer')
        comp_b = ' '.join(comp_b.lower().split())
        if comp_a != comp_b:
            break
        disc_a = job_a.get('title')
        disc_b = job_b.get('title')
        disc_a = ' '.join(disc_a.lower().split())
        disc_b = ' '.join(disc_b.lower().split())
        doc1 = nlp(disc_a)
        doc2 = nlp(disc_b)
        similar = doc1.similarity(doc2)
        print(doc1.similarity(doc2))
        if similar > 0.9:
            print('Clone Found: '+str(similar))
            clone = 1
            break
    if clone == 0:
        b = b.append(job_a)


def filter_boi(a):
    b = []
    for index_a in range(0, len(a)):
        check_concat(a, b, index_a)
    return b


pure_data = filter_fn(a)
print(pure_data)
