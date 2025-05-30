from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Password Manager API is running!"}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
