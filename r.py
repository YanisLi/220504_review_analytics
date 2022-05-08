import time
marks = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~' ]

def delete_marks(word, marks):
    for mark in word:
        if mark in marks:
            word = word.replace(mark, '')
    return word


time_start = time.time()

data = []
count = 0
with open('reviews.txt','r') as f: #以讀取模式讀取檔案，並稱他為f
	for line in f: #用for迴圈讀取f這個資料庫
		data.append(line) #把f這個程式讀取到data這個
		count += 1 #count = count + 1
		if count % 100000 == 0: # % 求餘數
		    print(len(data)) #每1000次輸出一次目前寫入的數字數
print('檔案讀取完畢，總共有 ',len(data),'筆資料')

word_count = {}

print('開始字典計數')
count_words = 0
for d in data:#for 迴圈讀取data這個資料庫，每一行為d
    words = d.split(' ')#把字用空白鍵分開來
    for word in words:#逐條跑word
        count_words += 1

        word = delete_marks(word, marks)

        if word in word_count:#檢查word是否出現過，如果有出現過
            word_count[word] += 1#字典value+1
        else:#如果沒有
            word_count[word] = 1#則新增一個key，並設定字數為1

        if count_words % 1000000 == 0:
            print('已經讀取', count_words, '字')

print('結束字典計數', '一共有', len(word_count), '不同的字')

print('開始輸出超過兩百次的字')
for word in word_count:
    if word_count[word] >= 200:
        print(word, word_count[word])
print('結束輸出超過兩百次的字')

time_end = time.time()
print('總運行時間', time_end - time_start, ' sec')

while True:
    word = input('請問你想查什麼字出現過幾次？，或q離開')
    if word == 'q':
        break
    elif word in word_count:
        print(word, '一共出現過',word_count[word])
    else:
        print(word, '沒有出現過喔')

print('程式結束')
# sum_len = 0
# for d in data:#每一筆資料叫做d，放在data
# 	sum_len += len(d)#把每一筆資料的長度都加進去sum_len的長度
# 	#print(sum_len)
# print('資料平均長度',sum_len/len(data))
#
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有',len(new),'筆留言小於100字元')
# print(new[0])
#
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有',len(good),'提到good')
#
# bad = [d for d in data if 'bad' in d]
# #d 把d裝進隊伍裡
# #for d in data 把1000000筆的留言一筆一筆叫出來，叫做d
# #if 'bad' in d 有沒有bad在裡面
# #output = [number-1] for number in reference if number%2 == 0]
# #number-1 運算、number 變數、reference 清單、if number%2==0 篩選清單
# print('一共有',len(bad),'提到bad')
