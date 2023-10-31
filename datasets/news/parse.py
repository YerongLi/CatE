# Read topic embeddings from emb_news_category_t.txt and create a dictionary
topic_embeddings = {}
with open('emb_news_category_t.txt', 'r') as topic_file:
    for line in topic_file:
        items = line.split()
        topic = items[0]
        vector = ' '.join(items[1:])
        topic_embeddings[topic] = vector

# Read word embeddings from emb_news_category_w.txt and create a dictionary
word_embeddings = {}
with open('emb_news_category_w.txt', 'r') as word_file:
    for line in word_file:
        items = line.split()
        word = items[0]
        vector = ' '.join(items[1:])
        word_embeddings[word] = vector

# Read words from res_news_category.txt and find their embeddings
categories = {}
for category, embeds in word_embeddings.items():
    if category in topic_embeddings:
        categories[category] = [f"{category} {topic_embeddings[category]}\n{category} {embeds}\n"]

# Save embeddings for each category into separate files
for category, embeds in categories.items():
    filename = f"{category}.terms.txt"
    with open(filename, 'w') as file:
        file.write(''.join(embeds))
