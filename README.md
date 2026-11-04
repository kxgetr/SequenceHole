# SequenceHole

İlk ve son sıra numarası arasındaki kayıp aralıkları sıkıştırır.

## Girdi

Tamsayı sıra numaraları.

## Kullanım

Python 3.11+, standart kütüphane.

```sh
python sequencehole.py input.json
python verify.py
```

Dosya verilmezse stdin okunur. Sonuç stdout üzerinde JSON olarak yazılır. Girdi hatası çıkış kodu 2 üretir.

Örnek sonuç:

```json
[
  [
    3,
    4
  ],
  [
    6,
    8
  ]
]
```
