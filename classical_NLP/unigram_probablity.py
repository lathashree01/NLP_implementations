def unigram_probability(corpus: str, word: str) -> float:
    if word not in corpus:
        return 0.0

    corp_list = corpus.split(" ")
    corp_counts = {}
    for w in corp_list:
        corp_counts[w] = corp_counts.get(w, 0) + 1
    
    word_count = corp_counts[word]
    return round(word_count/len(corp_list), 4)