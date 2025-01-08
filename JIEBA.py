import jieba
import json

# 要排除的token 词
excludes = ["将军", "却说"]

txt = open("./三国演义.txt", "r", encoding="utf-8").read()

# 分词切割
words = jieba.lcut(txt)

print("切割:", words)

counts = {}

# 哈希统计
for word in words:
    print("word", word)
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1


# 删除排除的分词token
for word in excludes:
    del counts[word]

print("counts:", json.dumps(counts, ensure_ascii=False, indent=4))

# 将对象hash表转换为列表，每一个元素是一个二元组
items = list(counts.items())

print("items:", items)

for i in range(1, 5):
    word, count = items[i]
    t = "{0:<10}{1:>5}"
    print(t.format(word, count, chr(12288)))
