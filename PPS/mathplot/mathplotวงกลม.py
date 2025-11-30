import matplotlib.pyplot as plt
genai = ['ChatGPT', 'Deepseek', 'Claude', 'Llama3', 'Gimini']
piesize = [30, 25, 20 ,15 ,10]
plt.pie(piesize, labels=genai, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  #ทำให้เป็นวงกลม
plt.title('genai market share 2025')
plt.show()