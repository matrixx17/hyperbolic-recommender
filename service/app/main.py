from fastapi import FastAPI, HTTPException, Query
from .service import query_similar
from .models import ItemSim

app = FastAPI(
    title="Hyperbolic Recommendation API",
    version="0.1.0",
    docs_url="/",
)

@app.get("/similar", response_model=list[ItemSim])
def similar(
    item_id: str = Query(..., description="Item ID (ASIN / SKU / node)"),
    k: int = Query(20, ge=1, le=100)
):
    try:
        return query_similar(item_id, k)
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
