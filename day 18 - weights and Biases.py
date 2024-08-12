import pandas as pd
import wandb

data = pd.read_csv('/content/drive/MyDrive/advertising.csv')
X = data[['TV', 'Radio', 'Newspaper']].values
Y = data['Sales'].values

dataset = pd.DataFrame({
    'TV': data['TV'], 'Radio': data['Radio'], 'Newspaper': data['Newspaper'], 'Sales': data['Sales']
})
def predict(x, w, b):
    return w * x + b

# Modified gradient function to return two values
def gradient(y_hat, y, x):
    dw = 2 * x * (y_hat - y)
    db = 2 * (y_hat - y)
    return dw, db # Return both dw and db

def update_weights(w, b, lr, dw, db):
    w_new = w - lr * dw
    b_new = b - lr * db
    return (w_new, b_new)

b = 1
w = 0
lr = 0.01
epochs = 1000

wandb.init(
    project = "demo-linear-regression",
    config = {
        "learning_rate": lr ,
        "epochs": epochs ,
    }
)
wandb.run.log({"Dataset": wandb.Table(dataframe = dataset)})

X_train = dataset[['TV', 'Radio', 'Newspaper']]
Y_train = dataset['Sales']

N = len(X_train)

losses = []

for epoch in range(epochs):
    for i in range(N):
        x = X_train.iloc[i] # Access the row as a Series
        y = Y_train.iloc[i]

        y_hat = predict(x, w, b)

        loss = ((y_hat - y) ** 2).sum() / 2
        wandb.log({"loss": loss})

        (dw, db) = gradient(y_hat=y_hat, y=y, x=x) # Now correctly unpacks two values

        w, b = update_weights(w, b, lr, dw, db)

wandb.finish()