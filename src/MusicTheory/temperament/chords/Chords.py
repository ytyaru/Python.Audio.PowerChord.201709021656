#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#各種音階における音程 29種類
class Chords:
    @classmethod
    def Get(cls, name=None):
        if None is name or '' == name: return [c for c in cls._chords if 'M' in c.names][0]
        for c in cls._chords:
            if name in c.names: return c
        raise Exception(f'"{name}"は存在しない和音名です。存在する和音名を指定して下さい。')
    
    _chords = []
    @classmethod
    def Load(cls):
        import csv
        from collections import namedtuple
        cls._chords.clear()
        with open('Chords.tsv', 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            header = next(reader)  # ヘッダーを読み飛ばす
            Chord = namedtuple('Chord', ('intervals','degreeNames','names','ja','en'))
            for row in reader:
#                print(row)
                #列数を超えた分は無視する
                if len(Chord._fields) < len(row): row = row[0:len(Chord._fields)-len(row)]
                #各列データをtupleにする
                for i, col in enumerate(row):
                    if 0 == i: row[i] = tuple([eval(v) for v in col.split(',')]) #`2-1+12`などの計算式を計算させる
                    else: row[i] = tuple(col.split(','))
                cls._chords.append(Chord._make(row))
#                print(cls._chords[-1])


if __name__ == '__main__':
    Chords.Load()
#    for c in Chords._Chords_chords: print(c)
    print(len(Chords._chords))
#    for c in Chords._chords: print(c)
    for c in Chords._chords:
        for name in c.names:
            print(Chords.Get(name))
    print('----- Get() -----')
    print(Chords.Get())
    print(Chords.Get(''))
    print(Chords.Get(None))
    print(Chords.Get('m7'))
    print(Chords.Get('存在しない名前'))
