from pydantic import BaseModel, Field


class ErrorResponseDto(BaseModel):
    """Error response."""

    error: str = Field(...)

    class Config:
        from_attributes = True


class MetadataDto(BaseModel):
    total: int = Field(0)
    last_page: int = Field(None)
    current_page: int = Field(1)
    per_page: int = Field(...)
    prev: int = Field(None)
    next: int = Field(None)

    class Config:
        from_attributes = True