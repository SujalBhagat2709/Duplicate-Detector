from similarity import get_similarity

def find_duplicates(texts, threshold=0.5):
    
    duplicates = []
    
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            
            score = get_similarity(texts[i], texts[j])
            
            if score >= threshold:
                duplicates.append((texts[i], texts[j], score))

    return duplicates


if __name__ == "__main__":
    
    data = [
        "python is great",
        "python is awesome",
        "machine learning is cool"
    ]
    
    result = find_duplicates(data)
    
    for r in result:
        print(r)