import pandas as pd
import tiktoken
from openai.embeddings_utils import get_embedding
import openai
openai.api_key = "<API_KEY>"

# embedding model parameters
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191

input_datapath = "Data.csv"  # to save space, we provide a pre-filtered dataset
df = pd.read_csv(input_datapath, index_col=0)
df = df[["_id", "productAsin", "username", "ratingScore", "reviewSummary", "reviewUrl","reviewReaction","reviewedIn","date","country", "countryCode","reviewDescription","isVerified","avatar","variant", "reviewImages","position"]]
df = df.dropna()
df["combined"] = (
    "Title: " + df.reviewSummary.str.strip() + "; Content: " + df.reviewDescription.str.strip()
)
df.head(2)

# subsample to 1k most recent reviews and remove samples that are too long
top_n = 1000


encoding = tiktoken.get_encoding(embedding_encoding)

# omit reviews that are too long to embed
df["n_tokens"] = df.combined.apply(lambda x: len(encoding.encode(x)))
df = df[df.n_tokens <= max_tokens].tail(top_n)
len(df)

# Ensure you have your API key set in your environment per the README: https://github.com/openai/openai-python#usage

# This may take a few minutes
df["embedding"] = df.combined.apply(lambda x: get_embedding(x, engine=embedding_model))
df.to_csv("Data_embedded.csv")