from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List, Dict, Any
import pandas as pd

class StorageError(Exception):
    """Base exception for storage errors."""
    pass

class DataStorage(ABC):
    """Abstract base class for data storage."""
    
    @abstractmethod
    def store_institutions(self, df: pd.DataFrame, source_type: str) -> None:
        """
        Store institution data.
        
        Args:
            df: DataFrame with institution data
            source_type: Type of institution ('bank' or 'credit_union')
        """
        pass
    
    @abstractmethod
    def store_quarterly_data(self, df: pd.DataFrame) -> None:
        """
        Store quarterly financial data.
        
        Args:
            df: DataFrame with quarterly data
        """
        pass
    
    @abstractmethod
    def get_institutions_by_asset_tier(
        self, min_assets: float, max_assets: float
    ) -> pd.DataFrame:
        """
        Get institutions within an asset range.
        
        Args:
            min_assets: Minimum total assets
            max_assets: Maximum total assets
            
        Returns:
            DataFrame of matching institutions
        """
        pass
    
    @abstractmethod
    def get_deposit_decline_institutions(
        self, threshold: float = 5.0
    ) -> pd.DataFrame:
        """
        Get institutions with significant deposit decline.
        
        Args:
            threshold: Decline percentage threshold
            
        Returns:
            DataFrame of institutions with deposits declining more than threshold
        """
        pass
