#lang racket

(require "../helper.rkt")

(define input (get-input 2018 1))
(define nums (map string->number (string-split input "\n")))
(define inp-len (length nums))

(displayln "Part 1:")
(displayln (number->string (sum nums)))

;; Int (Set Int) Int -> Int
(define part2-answer (let recur ([freq 0] [idx 0] [seen '()])
                       (fprintf (current-output-port) "~a ~a" freq idx)
                       (cond [(set-member? seen freq) freq]
                             [else 
                               (let* ([mod-idx (modulo idx inp-len)]
                                      [new-freq (+ freq (list-ref nums mod-idx))])
                                 (recur new-freq
                                        (+ idx 1) 
                                        (cons freq seen)))])))
(displayln "Part 2:")
(displayln (number->string part2-answer))
