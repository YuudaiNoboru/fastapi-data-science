import contextlib
import os

import joblib
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sklearn.pipeline import Pipeline

class PredictionInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    category: str

class NewsgroupsModel:
    model: Pipeline | None = None
    targets: list[str] | None = None
    def load_model(self) -> None:
        """Carrega o modelo"""
        model_file = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
        loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
        model, targets = loaded_model
        self.model = model
        self.targets = targets

    async def predict(self, input: PredictionInput) -> PredictionOutput:
        if not self.model or not self.targets:
            raise RuntimeError("O modelo não foi carregado.")
        prediction = self.model.predict([input.text])
        category = self.targets[prediction[0]]
        return PredictionOutput(category=category)

newgroups_model = NewsgroupsModel()

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    newgroups_model.load_model()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/prediction")
async def prediction(output: PredictionOutput = Depends(newgroups_model.predict)) -> PredictionOutput:
    return output