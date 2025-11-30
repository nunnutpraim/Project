import matplotlib.pyplot as plt
subjects = ['math', 'emglish', 'science', 'atr', 'thai']
scores = [85, 90, 87, 42, 99]
#plt.bar(subjects, scores, color='blue')
plt.bar(subjects, scores, color=['blue', 'red','pink','orange','black'])
plt.xlabel('subject')
plt.xlabel('scores')
plt.title('student score by subject')
plt.ylim(0,100)  #มีผลต่อการรันโค้ด
plt.show()