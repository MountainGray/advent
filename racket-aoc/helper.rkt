#lang racket

(provide get-input sum)

(define (read-file-as-string filename)
  (with-input-from-file filename
    (lambda ()
      (port->string (current-input-port)))))

(define (get-input year day)
  (let ([y (number->string year)]
        [d (number->string day)])
    (read-file-as-string (string-append "../../data/" y "/day" d ".txt"))))

(define sum (λ (nums) (foldl + 0 nums)))
