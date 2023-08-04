(defn reverte-lista [lista]
  (loop [lst lista, result '()]
    (if (empty? lst)
      result
      (recur (rest lst) (cons (first lst) result)))))


(defn rot-vec-esq [vetor]
  (loop [lst (rest (reverte-lista vetor)), result '()]
    (if (empty? lst)
      (cons (last vetor) result)
      (recur (rest lst) (cons (first lst) result)))))


(def u (rot-vec-esq '(1 2 3 4)))
(println u)
