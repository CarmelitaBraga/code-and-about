(defn fibonacci []
  (loop [a 0 b 1]
    (prn a)
      (recur b (+ a b))))

(fibonacci)

(defn fibonacci []
  (loop [a 0N b 1N]
    (prn a)
      (recur b (+ a b))))

(defn fibonacci []
  (loop [a 0 b 1]
    (prn a)
    (if (> a 2000)
      (prn "the end!")
      (recur b (+ a b)))))
