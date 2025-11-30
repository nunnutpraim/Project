import matplotlib.pyplot as plt
subjects = ['math', 'emglish', 'science', 'atr', 'thai']
scores = [85, 90, 87, 42, 99]
#plt.bar(subjects, scores, color='blue')
plt.barh(subjects, scores, color=['skyblue', 'red','pink','orange','purple'])
plt.ylabel('subject')
plt.xlabel('scores')
plt.title('student score by subject')
plt.xlim(0,100)  #มีผลต่อการรันโค้ด
plt.show()