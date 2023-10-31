# Read embeddings from emb_news_category_w.txt and create a dictionary
embeddings = {}

topic_embeddings = {}
with open('emb_news_category_t.txt', 'r') as topic_file:
    lines = topic_file.readlines()[1:]  # Exclude the first line
    for line in lines:
        items = line.split()
        topic = items[0]
        vector = ' '.join(items[1:])
        topic_embeddings[topic] = vector
print(topic_embeddings.keys())
with open('emb_news_category_w.txt', 'r') as emb_file:
    for line in emb_file:
        if len(line.strip()) > 0:
            items = line.split()
            word = items[0]
            vector = ' '.join(items[1:])
            embeddings[word] = vector

# Read words from res_news_category.txt and find their embeddings
categories = {}
with open('res_news_category.txt', 'r') as res_file:
    lines = res_file.readlines()
    for i in range(0, len(lines), 2):
        category_name = lines[i].split("Category (")[1].split("):")[0]
        words = lines[i + 1].strip().split(' ')
        category_embed = []
        for word in words:
            if word in embeddings:
                category_embed.append(f"{word} {embeddings[word]}")
        if category_name:
            categories[category_name] = category_embed[:10]  # Considering the first 10 embeddings

# Save word embeddings for each category into separate files
for category, embeds in categories.items():
    filename = f"{category}_terms.txt"
    with open(filename, 'w') as file:
        file.write('\n'.join(embeds))
