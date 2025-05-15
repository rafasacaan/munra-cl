from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship, Column, JSON
from datetime import datetime
import uuid

# Pydantic models for API requests/responses
class RecGenerationRequest(BaseModel):
    """
    Schema for title generation request.
    """
    topic: str
    ritual: str = "Restricciones"
    instrumento: str = "Ambiental"


class RecGenerationResponse(BaseModel):
    """
    Schema for title generation response.
    """
    rec: str


# SQLModel models for database
class RecGenerationHistory(SQLModel, table=True):
    """
    Model for storing rec generation history in the database.
    """
    __tablename__ = "rec_generation_history"
    
    # Main fields
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    topic: str
    ritual: str
    instrumento: str
    rec: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    rec: str
    user_id: Optional[str] = None
    ip_address: Optional[str] = None
    generation_time_ms: Optional[float] = None
    
    def from_request_response(
        request: RecGenerationRequest, 
        response: RecGenerationResponse,
        generation_time_ms: Optional[float] = None,
        ip_address: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> "RecGenerationHistory":
        """
        Create a history record from request and response objects.
        """
        return RecGenerationHistory(
            topic=request.topic,
            ritual=request.ritual,
            instrumento=request.instrumento,
            rec=response,
            generation_time_ms=generation_time_ms,
            ip_address=ip_address,
            user_id=user_id
        )


# Favorites model for future use
class RecFavorite(SQLModel, table=True):
    """Model for storing favorite recs."""
    __tablename__ = "title_favorites"
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    rec: str
    topic: str
    ritual: str
    instrumento: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Link to the generation history
    history_id: Optional[str] = Field(default=None, foreign_key="title_generation_history.id")
    
    # User information
    user_id: Optional[str] = None