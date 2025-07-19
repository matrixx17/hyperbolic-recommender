from typing import List
from .loader import index, STR2INT, INT2STR

def query_similar(item_id: str, k: int = 20) -> List[dict]:
    try:
        q_int = STR2INT[item_id]
    except KeyError:
        raise KeyError("unknown item_id")

    q_vec = index.get_items([q_int])

    # run k-NN search
    labels, dists = index.knn_query(q_vec, k=k)

    out = []
    for lid, dist in zip(labels[0], dists[0]):
        if lid == q_int:          # skip self
            continue
        out.append({"item_id": str(INT2STR[int(lid)]), "score": float(dist)})
    return out
