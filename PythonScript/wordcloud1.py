import wordcloud
w = wordcloud.WordCloud(width=1920,height=1080)
s = '''AttributeError: module 'wordcloud' has no attribute 'WordCloud' '''
w.generate(s)
w.to_file("wordcloud1.png")