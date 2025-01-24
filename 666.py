import torch
import torch.nn as nn
import numpy as np

# Шаг 1: Подготовка данных
texts = [
    "Твой первый текст",
    "Твой второй текст",
    # добавь сюда все свои тексты
]

# Токенизация текстов
tokenizer = {word: i for i, word in enumerate(set(' '.join(texts).split()))}
reverse_tokenizer = {i: word for word, i in tokenizer.items()}
sequences = [[tokenizer[word] for word in text.split()] for text in texts]

# Подготовка входных и выходных последовательностей
input_sequences = []
output_sequences = []

for seq in sequences:
    for i in range(1, len(seq)):
        input_sequences.append(seq[:i])
        output_sequences.append(seq[i])

max_length = max(len(x) for x in input_sequences)
input_sequences = [np.pad(seq, (0, max_length - len(seq)), mode='constant') for seq in input_sequences]

# Шаг 2: Создание модели
class TextGenerator(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size):
        super(TextGenerator, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x, _ = self.lstm(x.view(len(x), 1, -1))
        return self.fc(x.view(len(x), -1))

vocab_size = len(tokenizer)
embed_size = 10
hidden_size = 100

model = TextGenerator(vocab_size, embed_size, hidden_size)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

# Шаг 3: Обучение модели
input_tensor = torch.tensor(input_sequences)
output_tensor = torch.tensor(output_sequences)

for epoch in range(100):
    model.train()
    optimizer.zero_grad()
    output = model(input_tensor)
    loss = criterion(output, output_tensor)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch + 1}, Loss: {loss.item()}')

# Шаг 4: Генерация текста
def generate_text(seed_text, next_words=10):
    model.eval()
    for _ in range(next_words):
        token_list = [tokenizer[word] for word in seed_text.split()]
        token_list = torch.tensor(np.pad(token_list, (0, max_length - len(token_list)), mode='constant')).unsqueeze(0)
        predicted = model(token_list)
        predicted_word_index = torch.argmax(predicted[-1]).item()
        seed_text += " " + reverse_tokenizer[predicted_word_index]
    return seed_text

# Пример использования
print(generate_text("Твой пример текста", next_words=5))
