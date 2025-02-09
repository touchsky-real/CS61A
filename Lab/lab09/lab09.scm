(define (over-or-under num1 num2)
  ; (cond
  ;     ((< num1 num2) -1)
  ;     ((= num1 num2) 0)
  ;     (else 1)
  ; )
  (if (< num1 num2) -1 (if (= num1 num2) 0 1))
)

(define (make-adder num)
  ; (lambda (inc) (+ num inc))
  (define (adder inc) (+ num inc))
  adder
)

(define (composed f g)
  (define (f_of_g_of x) (f (g x)))
  f_of_g_of
)

(define (repeat f n)
  (if(= n 0)
    (lambda (x) x)
    (composed f (repeat f (- n 1)))
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (define big (max a b))
  (define small (min a b))
  (define remainder (modulo big small))
  (if (zero? remainder)
    small
    (gcd small remainder)
  )
)
