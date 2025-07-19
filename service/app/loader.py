import pathlib, pickle, hnswlib, numpy as np

MODELDIR = pathlib.Path(__file__).resolve().parents[1] / "models"

IDX_PATH = MODELDIR / "item_hnsw.bin"
index = hnswlib.Index(space="l2", dim=33)
index.load_index(str(IDX_PATH), max_elements=0)     # O(1) RAM copy
index.set_ef(128)                                  

with open(MODELDIR / "id_map.pkl", "rb") as f:
    maps = pickle.load(f)
STR2INT = maps["str_to_int"]
INT2STR = maps["int_to_str"]         # NumPy array indexed by int id
