data = []
with open('reviews.txt','r') as f:#以讀取模式讀取檔案，並稱他為f
	for line in f:#用for迴圈讀取f這個資料庫
		data.append(line)#把f這個程式讀取到data這個
print(len(data))
print(data[0])
print('-----------------')
print(data[1])