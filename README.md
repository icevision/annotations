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

| Seq. name | FLIF | JPEG | WebM | Annotations | Frames |
| --------- | ---- | ---- | ---- | ----------- | ------ |
| `2018-02-13_1418_left` | [link](http://oscar.skoltech.ru/data/2018-02-13_1418/left.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1418/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1418/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-02-13_1418_left) | All |
| `2018-02-13_1523_left` | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.webm) | Not ready | 0-5000 |
| `2018-03-07_1322_right` | [link](http://oscar.skoltech.ru/data/2018-03-07_1322/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1322/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1322/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1322_right) | All |
| `2018-03-07_1325_left` | [link](http://oscar.skoltech.ru/data/2018-03-07_1325/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1325/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1325/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1325_left) | All |
| `2018-03-07_1336_right` | [link](http://oscar.skoltech.ru/data/2018-03-07_1336/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1336/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1336/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1336_right) | All |
| `2018-03-07_1357_right` | [link](http://oscar.skoltech.ru/data/2018-03-07_1357/right.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1357/right_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-07_1357/right.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-07_1357_right) | All |
| `2018-03-16_1316_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1316/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1316/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1316/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-16_1316_left) | All |
| `2018-03-16_1324_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-16_1324_left) | All |
| `2018-03-16_1347_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1347/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1347/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1347/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-16_1347_left) | All |
| `2018-03-16_1418_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1418/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1418/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1418/left.webm) | [link](https://github.com/icevision/annotations/tree/master/training/2018-03-16_1418_left) | All |
## Test sequences

| Seq. name | FLIF | JPEG | WebM | Frames |
| --------- | ---- | ---- | ---- | ------ |
| `2018-03-16_1324_left` | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-03-16_1324/left.webm) | All |
| `2018-02-13_1523_left` | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left_jpgs.tar) | [link](http://oscar.skoltech.ru/data/2018-02-13_1523/left.webm) | 5001-end |

## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">IceVisionSet</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName"><a href="https://www.skoltech.ru/">ISR Lab, Skoltech</a> & <a href="https://www.rvc.ru/">RVC</a></span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="http://oscar.skoltech.ru" rel="dct:source">http://oscar.skoltech.ru/</a>.
