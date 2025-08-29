import math

def calculate_idf(all_documents):
    term_count = {}
    for document in all_documents:
        unique_terms = set(document)
        for term in unique_terms:
            term_count[term] = term_count.get(term, 0) + 1
        

    idf_values = {term: math.log(len(all_documents) / count) for term, count in term_count.items()}
    return idf_values

def score(query, document, operation_type, all_documents, idf_values):
    if operation_type == 'and':
        if set(query).issubset(document):
            return sum(tf(token, document) * idf_values[token] for token in query)
        else:
            return 0
    else:
        return sum(tf(token, document) * idf_values[token] for token in query if token in document)

def tf(token, document):
    return float(document.count(token)) / len(document) if len(document) > 0 else 0