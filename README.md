# Hyperbolic Recommender (MVP)

This project was inspired by my research in Cornell's RelaxML Laboratory. 

HyperRec is a hierarchy-aware item-to-item recommendation system that run **entirely on CPU** and answer in **\< 10 ms** using 33-dim hyperbolic embeddings and an HNSW index.

---

## Motivation
* Tree-shaped catalogues (ex: e-commerce, document categories, org charts) are inefficiently captured by Euclidean cosine vectors.  
* A closed-form hyperbolic heat kernel preserves that hierarchy in only 32
  learned dimensions (raised to 33 for the hyperboloid model).  
* All heavy computation happens offline; the online layer is a lightweight FastAPI
  app that memory-maps a 22 MB HNSW graph (for the sample Amazon Electronics Reviews Dataset)

---


While the MVP is functional in its current state, I'm currently working on some refinements to improve functionality. Installation instructions will be added soon. 
