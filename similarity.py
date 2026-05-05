def get_similarity(a, b):
    
    set_a = set(a.split())
    set_b = set(b.split())
    
    common = set_a.intersection(set_b)
    
    score = len(common) / max(len(set_a), len(set_b))
    
    return score


if __name__ == "__main__":
    
    s1 = "python is great"
    s2 = "python is awesome"
    
    print("Similarity:", get_similarity(s1, s2))