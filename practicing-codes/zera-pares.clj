(defn reverte-lista [lista]
  (loop [lista lista, result '()]
    (if (empty? lista)
      result
      (recur (rest lista) (cons (first lista) result)))))

(def c '(5 4 3 2 1))
(def t (reverte-lista c))
(prn t)

(def x '(1 4 9 16 25 36 49 64 81 100))
(defn zera-pares [lista]
  (reverte-lista lista)
  (loop [result '(), lst (reverte-lista lista)]
    (if (empty? lst)
      result
    (recur (if (even? (first lst)) (cons 0 result) (cons (first lst) result)) (rest lst)))))
    ;(if (even? (first lst))
     ; (cons 0 result)
      ;(cons (first lst) result))
    ;(recur (rest lst))))

(prn x)
(def g (zera-pares x))
(prn g)

