# IceVisionSet annotation files

This repository contains manual annotations of traffic signs. Images can be
downloaded from http://oscar.skoltech.ru/data/.

## Annotations format

Annotations for each sequence are stored inside folders in the form of TSV files.
Each TSV file has the following fields:
- `class`: traffic sign code according to Russian traffic code. See [wiki] for
full list of signs.
- `xtl`, `ytl`, `xbr`, `ybr`: bounding box coordinates. `xbr` is always bigger than `xtl` and `ybr` is always bigger than `ytl`.
- `temporary`: is sign for "temporary" (i.e. has yellow background)?
- `occluded`: is sign occluded?
- `data`: associated data, e.g. speed limit, distance, names, etc.

Some files also contain `manual` field, used to denote if bounding box was
annotated manually (`true`) or was linearly interpolated (`false`).

`class` has two additionall special values:
- `8`: used for additional information signs for which exact code can not be
determined
- `NA`: used for unofficial or unrecognizable signs.

[wiki]: https://ru.wikipedia.org/wiki/Дорожные_знаки_России

## Training sequences

| Seq. name | FLIF | JPEG | WebM | Annotations | Frames | Annotated | Boxes |
| --------- | ---- | ---- | ---- | ----------- | ------ | --------- | ----- |
| `2018-02-13_1418_left` | [link](http://oscar.skoltech.ru/data/2018-02-13_1418/left.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1418/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1418/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-02-13_1418_left) | 23652 | 788 | 4737 |
| `2018-02-13_1523_left` | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.webm) | Not ready | 0-5000 | - | - |
| `2018-03-02_1239_right` | [link](http://oscar.skoltech.ru/data/2018-03-02_1239/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-02_1239/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-02_1239/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1322_right) | 9688 | 323 | 2726 |
| `2018-03-07_1322_right` | [link](http://oscar.skoltech.ru/data/2018-03-07_1322/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1322/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1322/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1322_right) | 4312 | 145 | 247 |
| `2018-03-07_1325_left` | [link](http://oscar.skoltech.ru/data/2018-03-07_1325/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1325/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1325/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1325_left) | 6318 | 208 | 362 |
| `2018-03-07_1336_right` | [link](http://oscar.skoltech.ru/data/2018-03-07_1336/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1336/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1336/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1336_right) | 29374 | 975 | 3604 |
| `2018-03-07_1354_right` | [link](http://oscar.skoltech.ru/data/2018-03-07_1354/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1354/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1354/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1357_right) | 3032 | 102 | 143 |
| `2018-03-07_1357_right` | [link](http://oscar.skoltech.ru/data/2018-03-07_1357/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1357/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1357/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1357_right) | 16742 | 557 | 2536 |
| `2018-03-16_1316_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1316/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1316/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1316/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-16_1316_left) | 14208 | 474 | 2550 |
| `2018-03-16_1347_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1347/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1347/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1347/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-16_1347_left) | 14185 | 332 | 507 |
| `2018-03-16_1418_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1418/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1418/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1418/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-16_1418_left) | 659 | 21 | 36 |

## Test sequences

| Seq. name | FLIF | JPEG | WebM | Annotations | Frames | Annotated | Boxes |
| --------- | ---- | ---- | ---- | ----------- | ------ | --------- | ----- |
| `2018-02-13_1523_left` | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.webm) | [link](https://github.com/icevision/annotations/tree/master/test/2018-02-13_1523_left) | 5001-36365 | 1048 | 4829 |
| `2018-03-16_1324_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left.webm) | [link](https://github.com/icevision/annotations/tree/master/test/2018-03-16_1324_left) | 39431 | 1310 | 6479 |

## Final sequences

Encrypted archives can be downloaded from http://oscar.skoltech.ru/data/online_final/.
Password for `test_archive.zip` is "password". Password for other archives is
"15498_15532_e8".

SHA-256 hash sums:

```
f7c7edd5379a27b334542b7219276d79ae7670098327a3017c92d142cb386cdd  flifs.zip
5250a0c7b72ed3e61cee22318f69812cdfd260d1fd227a6e0035bb6c4852746e  jpgs.zip
86729a19867147709fbc0c21486f0d9d33ddecb72e351368810b9ff0f3f8eea8  webms.zip
6730558c937ed100b8411dc7c126e3c9d992c68ffa8a7856650e224f6f8098ff  test_archive.zip
```

Sequences table:

| Seq. name | Frames | Annotated | Boxes |
| --------- | ------ | --------- | ----- |
| `2018-02-16_1515_left` | 3676 | 123 | 553 |
| `2018-03-16_1424_left` | 2785 | 94 | 402 |
| `2018-03-23_1352_right` | 8539 | 287 | 1856 |

## Annotation errors

If you'll encounter any annotation errors, feel free to open an issue
describing them, but please be specific and do not forget to list frames in
question.

## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">IceVisionSet</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName"><a href="https://www.skoltech.ru/">ISR Lab, Skoltech</a> & <a href="https://www.rvc.ru/">RVC</a></span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="http://oscar.skoltech.ru" rel="dct:source">http://oscar.skoltech.ru/</a>.
