
# Read embeddings from emb_news_category_w.txt and create a dictionary
embeddings = {}
with open('emb_news_category_w.txt', 'r') as emb_file:
    for line in emb_file:
        if len(line.strip()) > 0:
            items = line.split()
            word = items[0]
            vector = [float(val) for val in items[1:]]
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
                category_embed.append(embeddings[word])
        if category_name:
            categories[category_name] = category_embed[:10]  # Considering the first 10 embeddings

# Display or process the obtained word embeddings for each category
for category, embeds in categories.items():
    print(f"Category: {category}")
    for i, emb in enumerate(embeds):
        print(f"Word {i + 1}: {emb}")

