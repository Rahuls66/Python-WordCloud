import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from wordcloud import WordCloud

df = pd.read_csv("android-games.csv")

df.head()

text = ", ".join(cat.split()[1] for cat in df.category)

wordcloud = WordCloud(collocations = False, background_color = 'white').generate(text)


# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
