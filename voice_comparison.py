from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def get_top_similar(file, top):
    top_names = []

    wav = preprocess_wav(file)
    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav)

    cs = cosine_similarity(X=embeded_voices, Y=embed.reshape(1, -1))
    cs_sorted = np.argsort(cs, axis=0)[::-1][:, 0]
    top_similarity = cs[cs_sorted[:top]]
    top_ids = ids[cs_sorted[:top]]

    for each in top_ids:
        top_names.append(mydict[each])

    return top_names, top_similarity, top_ids

# IMPORT DATA

df = pd.read_csv("ids_names.csv")
mydict = dict(zip(df.id,df.name)) #Creates dictionary id - celebrity
embeded_voices = np.load("embeded_voices.npy")
ids = np.load("ids_voices.npy")

top = 5

names, scores, res_ids = get_top_similar("your_audio.wav", top = top)
print("\nYour best match is {} with {:.0f}% similarity.".format(names[0].replace("_"," "),scores[0][0]*100))

print("\n Your top {} is the following:".format(top))

for name in names:
    print("\n" + name.replace("_", " "))