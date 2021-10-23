# factoradic
Generate a 128-bit number from a shuffled deck of cards.

Given a shuffled deal of cards like:
```
['3c', 'Qh', 'Kd', '6c', '7c', '8c', '6h', '9c', '10c', 'Jc', '10d', 'Kc', 'Ac',
 '2d', '3d', '4d', '5d', '6d', '4s', '10s', 'Js', '9h', '7h', 'Jh', 'Jd', '3s',
 'Ks', 'Qd', '2s', '8d', '5h', 'Ad', 'As', '9d', '7s', '3h', 'Qc', 'Kh', '8h',
 '9s', '4c', '5c', '4h', 'Qs', '10h', '6s', '5s', '7d', '2c', '2h', '8s', 'Ah']
```
Calculate a 128-bit number.

NOTE: since 52! > 2**128, a number of deck shufflings will share the same 128-bit number.

For example, the above deck shuffling and the below shuffling both map to the same number:
```
['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac',
 '2d', '3d', '4d', '5d', '6d', '8h', '4h', 'Qs', '9h', 'Js', '8d', 'Qd', '4s',
 'Qh', '7s', '6h', '2h', '2s', 'Kh', '10s', '5h', 'Jh', '3h', 'Ah', '6s', '3s',
 '9s', '10d', '10h', 'Ks', '7h', 'Ad', 'As', '9d', '7d', 'Jd', 'Kd', '8s', '5s']
```

That number is:  `124439904724342638525433701090112646041`

# To generate a 128-bit number from a deck shuffling:
```
>>> from factoradic import deck_to_number
>>> 
>>> deck = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac',
...  '2d', '3d', '4d', '5d', '6d', '8h', '4h', 'Qs', '9h', 'Js', '8d', 'Qd', '4s',
...  'Qh', '7s', '6h', '2h', '2s', 'Kh', '10s', '5h', 'Jh', '3h', 'Ah', '6s', '3s',
...  '9s', '10d', '10h', 'Ks', '7h', 'Ad', 'As', '9d', '7d', 'Jd', 'Kd', '8s', '5s']
>>> 
>>> deck_to_number(deck=deck)
124439904724342638525433701090112646041
>>>
```

# To run tests:
```
$ python -m unittest -vv
test_factoradic (test_factoradic.TestFactoradic) ... 

number: 86147408288686326839861397527590576950

shuffled deck: ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ac',
                '2d', '3d', '4d', '5d', '6d', '3h', 'Qs', '7h', 'Ah', '3s', 'Js', 'Kd', 'Ks',
                '10d', '4h', '9s', '10s', '8h', '8s', 'Jh', '5h', '4s', 'Qd', 'As', 'Qh', 'Ad',
                '7d', '9h', 'Kh', '7s', '5s', '6s', '2s', '2h', '9d', 'Jd', '8d', '6h', '10h']

ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

```
