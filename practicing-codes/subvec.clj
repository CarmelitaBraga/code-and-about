(defn sublist [lista start end]
  (loop [i start, result []]
    (if (> i end)
      result
      (recur (conj result (get lista i)) (inc i)))))

(def x [1 2 5 8  6 78 29 63 41])
(def y (sublist x 3 7))
(prn y)
