def book_pairs(books):
    books.sort(reverse=True)
    print(books)
    
    envelopes = []
    visited_i = set()
    i, j = 0, len(books) - 1
    
    while len(visited_i) < len(books):
        if i in visited_i:
            i += 1
            continue
        
        if j in visited_i:
            j -= 1
            continue
            
        peso_juntos = books[i] + books[j]
        
        if peso_juntos <= 1:
            envelopes.append((i+1, j+1, peso_juntos)) if i != j else envelopes.append((i+1, peso_juntos))
            visited_i.add(i)
            visited_i.add(j)
            i, j = 0, len(books)-1
        else:
            j -= 1
    
    return envelopes




lista = [0.58, 0.75, 0.2, 0.5, 0.9, 0.25, 0.1, 0.15, 0.4]
print(book_pairs(lista))