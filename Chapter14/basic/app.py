"""Módulo responsável por criar rota para geração de imagem"""

from dramatiq import Message
from fastapi import FastAPI, status
from pydantic import UUID4, BaseModel, Field

from Chapter14.basic.worker import text_to_image_task


class ImageGenerationInput(BaseModel):
    """Classe para entrada de informações para geração de imagem"""
    prompt: str
    negative_prompt: str
    num_steps: int = Field(50, gt=0, le=50)


class ImageGenerationOutput(BaseModel):
    """Classe para saída de geração de imagem"""
    task_id: UUID4


app = FastAPI()


@app.post(
    "/image-generation",
    response_model=ImageGenerationOutput,
    status_code=status.HTTP_202_ACCEPTED,
)
async def post_image_generation(entrada: ImageGenerationInput) -> ImageGenerationOutput:
    """Função para chamada da geração de imagem"""
    task: Message = text_to_image_task.send(
        entrada.prompt, negative_prompt=entrada.negative_prompt, num_steps=entrada.num_steps
    )
    return ImageGenerationOutput(task_id=task.message_id)
