import threading
import time

# 子執行緒的工作函數
def job(num):
  print("Thread", num)
  for i in range(5):
    print(str(num) +" / "+ str(i))
    time.sleep(1)

# 建立 5 個子執行緒
threads = []
for i in range(5):
  threads.append(threading.Thread(target = job, args = (i,)))
  #threads[i].start()


for i in range(5):  
  threads[i].start()
# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
for i in range(5):
  threads[i].join()

print("Done.")