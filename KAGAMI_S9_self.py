import hashlib, sys

with open(__file__, 'rb') as f:
    data = f.read()

h = hashlib.sha256(data).hexdigest()

# ハッシュの偶数桁のみ抽出（0,2,4,6,8,10,12桁目）
extracted = ''.join([h[i] for i in range(0, 14, 2)])

print(h)
print()
print("抽出値:", extracted)
print()

# 抽出値から座標を計算
val = int(extracted, 16)
coord = val % 10000
print(f"座標: {coord}")
print(f"次のURL: k4g4m1.jp/prove?id={coord:04d}")
