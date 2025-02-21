from collections import Counter
# with open('document.txt', 'r') as file:
#     document = file.read()
document='''Bootstrap CSS is a free, open-source framework that provides pre-built HTML, CSS, and JavaScript components to quickly develop responsive and mobile-first websites, essentially offering a collection of ready-to-use styles for elements like buttons, forms, navigation, and grids, allowing developers to build webpages faster without writing extensive custom CSS code from scratch. 
Key points about Bootstrap CSS'''

Bootstrap="Bootstrap"
word_count=Counter(document)
for word,count in word_count.most_common(10):
    print(word, count) 

