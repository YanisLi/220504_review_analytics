data = []
count = 0
with open('reviews.txt','r') as f: #以讀取模式讀取檔案，並稱他為f
	for line in f: #用for迴圈讀取f這個資料庫
		data.append(line) #把f這個程式讀取到data這個
		count += 1 #count = count + 1
		if count % 1000 == 0: # % 求餘數
		    print(len(data)) #每1000次輸出一次目前寫入的數字數
print('檔案讀取完畢，總共有 ',len(data),'筆資料')

sum_len = 0
for d in data:#每一筆資料叫做d，放在data
	sum_len += len(d)#把每一筆資料的長度都加進去sum_len的長度
	#print(sum_len)
print('資料平均長度',sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆留言小於100字元')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'提到good')

bad = [d for d in data if 'bad' in d]
#d 把d裝進隊伍裡
#for d in data 把1000000筆的留言一筆一筆叫出來，叫做d
#if 'bad' in d 有沒有bad在裡面
#output = [number-1] for number in reference if number%2 == 0]
#number-1 運算、number 變數、reference 清單、if number%2==0 篩選清單
print('一共有',len(bad),'提到bad')





