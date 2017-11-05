# このソフトウェアについて

和音(和声音)データをTSVファイル化し、コードネームで取得できるようにした。

# 対象ファイル名

ファイル名|説明
----------|----
MusicTheory/temperament/chords/Chords.py|和音データの読込と取得
MusicTheory/temperament/chords/Chords.tsv|和音データ
MusicTheory/temperament/chords/ChordIntervals.py|各スケールの構成音を生成して音声ファイルを出力する

# 実行

```sh
$ python Chords.py 
29
Chord(intervals=(0, 7), degreeNames=('P1', 'P5'), names=('pow',), ja=('空虚五度', 'パワーコード'), en=('OpenFifth', 'Power'))
Chord(intervals=(0, 12), degreeNames=('P1', 'P8'), names=('oct',), ja=('オクターブ奏法',), en=('Octave',))
Chord(intervals=(0, 4, 7), degreeNames=('P1', 'M3', 'P5'), names=('M', '△'), ja=('長三和音',), en=('Major',))
Chord(intervals=(0, 4, 7), degreeNames=('P1', 'M3', 'P5'), names=('M', '△'), ja=('長三和音',), en=('Major',))
Chord(intervals=(0, 3, 7), degreeNames=('P1', 'm3', 'P5'), names=('m',), ja=('短三和音',), en=('Minor',))
Chord(intervals=(0, 4, 8), degreeNames=('P1', 'm3', 'a5'), names=('aug',), ja=('増三和音',), en=('Augmented',))
Chord(intervals=(0, 3, 6), degreeNames=('P1', 'm3', 'd5'), names=('dim',), ja=('減三和音',), en=('Diminished',))
Chord(intervals=(0, 4, 7, 10), degreeNames=('P1', 'M3', 'P5', 'm7'), names=('7',), ja=('属七の和音',), en=('Seventh',))
Chord(intervals=(0, 3, 7, 10), degreeNames=('P1', 'm3', 'P5', 'm7'), names=('m7',), ja=('短七の和音',), en=('MinorSeventh',))
Chord(intervals=(0, 4, 7, 11), degreeNames=('P1', 'm3', 'P5', 'M7'), names=('M7',), ja=('長七の和音',), en=('MajorSeventh',))
Chord(intervals=(0, 3, 6, 9), degreeNames=('P1', 'm3', 'd5', 'd7'), names=('dim7',), ja=('減七の和音',), en=('DiminishedSeventh',))
Chord(intervals=(0, 4, 8, 11), degreeNames=('P1', 'M3', 'a5', 'M7'), names=('M7+5',), ja=('増七の和音',), en=('AugmentedSeventh',))
Chord(intervals=(0, 3, 6, 10), degreeNames=('P1', 'm3', 'd5', 'm7'), names=('m7-5',), ja=('減五短七の和音',), en=('HalfDiminishedSeventh',))
Chord(intervals=(0, 3, 7, 11), degreeNames=('P1', 'm3', 'P5', 'M7'), names=('mM7',), ja=('短三長七の和音',), en=('MinorMajorSeventh',))
Chord(intervals=(0, 4, 7, 9), degreeNames=('P1', 'M3', 'P5', 'M6'), names=('C6',), ja=('メジャーシックスス',), en=('MajorSixth',))
Chord(intervals=(0, 3, 7, 9), degreeNames=('P1', 'm3', 'P5', 'M6'), names=('Cm6',), ja=('マイナーシックスス',), en=('MinorSixth',))
Chord(intervals=(0, 4, 7, 10, 14), degreeNames=('P1', 'M3', 'P5', 'm7', 'M9'), names=('9',), ja=('長九の和音',), en=('Ninth',))
Chord(intervals=(0, 4, 7, 10, 13), degreeNames=('P1', 'M3', 'P5', 'm7', 'm9'), names=('7-9',), ja=('短九の和音',), en=('MajorNinth',))
Chord(intervals=(0, 4, 7, 10, 15), degreeNames=('P1', 'M3', 'P5', 'm7', 'a9'), names=('7+9',), ja=('セブンスシャープナインス',), en=('SeventhSharpNinth',))
Chord(intervals=(0, 5, 7), degreeNames=('P1', 'P4', 'P5'), names=('sus4',), ja=('サスフォー',), en=('Sus4',))
Chord(intervals=(0, 5, 7, 10), degreeNames=('P1', 'P4', 'P5', 'm7'), names=('7sus4',), ja=('セブンスサスフォー',), en=('SeventhSus4',))
Chord(intervals=(0, 2, 7), degreeNames=('P1', 'M2', 'P5'), names=('sus2',), ja=('サスツー',), en=('Sus2',))
Chord(intervals=(0, 4, 7, 10, 18), degreeNames=('P1', 'M3', 'P5', 'm7', 'a11'), names=('7+11',), ja=('セブンスシャープイレブン',), en=('SeventhSharp11th',))
Chord(intervals=(0, 4, 7, 11, 18), degreeNames=('P1', 'm3', 'P5', 'M7', 'a11'), names=('M7+11',), ja=('メジャーセブンスシャープイレブン',), en=('MajorSeventhSharp11th',))
Chord(intervals=(0, 4, 10, 21), degreeNames=('P1', 'M3', 'm7', 'M13'), names=('7(13)',), ja=('セブンスサーティーンス',), en=('Seventh13th',))
Chord(intervals=(0, 4, 10, 20), degreeNames=('P1', 'M3', 'm7', 'm13'), names=('7(b13)',), ja=('セブンスフラットサーティーンス',), en=('SeventhFlat13th',))
Chord(intervals=(0, 4, 7, 14), degreeNames=('P1', 'M3', 'P5', 'M9'), names=('add9',), ja=('アドナインス',), en=('Add9th',))
Chord(intervals=(0, 4, 5, 7), degreeNames=('P1', 'M3', 'P4', 'P5'), names=('add4',), ja=('アドフォー',), en=('Add4',))
Chord(intervals=(0, 4, 6), degreeNames=('P1', 'M3', 'd5'), names=('-5',), ja=('ディムフィフス',), en=('Dim5th',))
Chord(intervals=(0, 4, 6, 10), degreeNames=('P1', 'M3', 'd5', 'm7'), names=('C7-5',), ja=('セブンスディムフィフス',), en=('SeventhDim5th',))
----- Get() -----
Chord(intervals=(0, 4, 7), degreeNames=('P1', 'M3', 'P5'), names=('M', '△'), ja=('長三和音',), en=('Major',))
Chord(intervals=(0, 4, 7), degreeNames=('P1', 'M3', 'P5'), names=('M', '△'), ja=('長三和音',), en=('Major',))
Chord(intervals=(0, 4, 7), degreeNames=('P1', 'M3', 'P5'), names=('M', '△'), ja=('長三和音',), en=('Major',))
Chord(intervals=(0, 3, 7, 10), degreeNames=('P1', 'm3', 'P5', 'm7'), names=('m7',), ja=('短七の和音',), en=('MinorSeventh',))
Traceback (most recent call last):
  File "Chords.py", line 46, in <module>
    print(Chords.Get('存在しない名前'))
  File "Chords.py", line 9, in Get
    raise Exception(f'"{name}"は存在しない和音名です。存在する和音名を指定して下さい。')
Exception: "存在しない名前"は存在しない和音名です。存在する和音名を指定して下さい。
```

# 課題

* 和音パターンを調査し網羅したい
    * 和声音でも未実装パターンがある
        * 名前で取得したい
            * 転回も指定したい
                * omit(音を抜くヴォイシング)も指定したい
    * 非和声音は勉強不足。難しそう……
* 12平均律以外の音律でも構成音を算出したいが……
    * 純正律における中間の5音も算出したい。計算方法がよくわからない
* 純正律で綺麗な和音になる主要三和音とそれ以外の音痴な副和音を聴き比べてみたい
* ソースコードが整理できていない
    * 音楽理論がわからず、どうまとめていいのかもわからない

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## 和音

* https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3
* http://www.piano-c.com/

## 音程

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E7%A8%8B
* https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1365320628
* https://okwave.jp/qa/q6858420.html

## 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

## 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

## 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

## 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

### 五度圏

* http://dn-voice.info/music-theory/godoken/

## 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

## サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

