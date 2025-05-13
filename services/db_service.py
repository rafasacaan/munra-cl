from sqlmodel import Session, select
from models.database import RecGenerationHistory, RecGenerationRequest, RecGenerationResponse, RecFavorite
from typing import List, Optional
import time

class DBService:
    """
    Service for database operations.
    """
    
    def __init__(self, session: Session):
        """Initialize the DB service.
        
        Args:
            session: SQLModel database session
        """
        self.session = session
    

    async def record_rec_generation(
        self,
        request: RecGenerationRequest,
        response: RecGenerationResponse,
        start_time: Optional[float] = None,
        ip_address: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> RecGenerationHistory:
        """Record a rec generation interaction in the database.
        
        Args:
            request: The title generation request
            response: The title generation response
            start_time: Optional start time for timing the generation
            ip_address: Optional IP address of the requester
            user_id: Optional user ID
            
        Returns:
            The saved history record
        """
        # Calculate generation time if start_time was provided
        generation_time_ms = None
        if start_time is not None:
            generation_time_ms = (time.time() - start_time) * 1000
            
        # Create the history record
        history = RecGenerationHistory(
            topic=request.topic,
            ritual=request.ritual,
            instrumento=request.instrumento,
            rec=response,
            generation_time_ms=generation_time_ms,
            ip_address=ip_address,
            user_id=user_id
        )
        # Save to database
        self.session.add(history)
        self.session.commit()
        self.session.refresh(history)
        return history
        

    def get_recent_generations(
        self, 
        limit: int = 10
    ) -> List[RecGenerationHistory]:
        """Get recent title generation history.
        
        Args:
            limit: Maximum number of records to return
            
        Returns:
            List of history records
        """
        statement = select(RecGenerationHistory).order_by(RecGenerationHistory.created_at.desc()).limit(limit)
        results = self.session.exec(statement).all()
        return results
    

    def add_favorite(
        self,  
        topic: str,
        ritual: str,
        instrumento: str,
        history_id: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> RecFavorite:
        """Add a title to favorites.
        
        Args:
            title: The title to favorite
            topic: The topic of the title
            platform: The platform for the title
            style: The style of the title
            history_id: Optional ID of the generation history record
            user_id: Optional user ID
            
        Returns:
            The saved favorite record
        """
        favorite = RecFavorite(
            topic=topic,
            ritual=ritual,
            instrumento=instrumento,
            history_id=history_id,
            user_id=user_id
        )
        
        self.session.add(favorite)
        self.session.commit()
        self.session.refresh(favorite)
        
        return favorite
        
    def get_favorites(self, user_id: Optional[str] = None, limit: int = 50) -> List[RecFavorite]:
        """Get favorite titles.
        
        Args:
            user_id: Optional user ID to filter by
            limit: Maximum number of records to return
            
        Returns:
            List of favorite records
        """
        statement = select(RecFavorite)
        
        if user_id:
            statement = statement.where(RecFavorite.user_id == user_id)
            
        statement = statement.order_by(RecFavorite.created_at.desc()).limit(limit)
        results = self.session.exec(statement).all()
        
        return results