from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Dict, Any
import pandas as pd

class DataSourceError(Exception):
    """Base exception class for [DataSource] errors."""
    pass

class DataValidator:
    """Validates and normalizes data from [DataSource]"""

    @staticmethod
    def validate_institution_data(df: pd.DataFrame) -> None:
        """Validate institution data structure."""
        required_cols = {'charter_number', 'web_domain', 'city', 'state'}
        missing = required_cols - set(df.columns)
        if missing:
            raise DataSourceError(f"Missing required columns: {missing}")

    @staticmethod
    def validate_quarterly_data(df: pd.DataFrame) -> None:
        """Validate quarterly data structure."""
        required_cols = {
            'charter_number', 
            'quarter_end_date', 
            'total_assets', 
            'total_deposits'
        }
        missing = required_cols - set(df.columns)
        if missing:
            raise DataSourceError(f"Missing required columns: {missing}")

class DataSource(ABC):
    """Abstract base class for financial data sources."""

    def __init__(self, validator: Optional[DataValidator] = None):
        validator = validator or DataValidator()
        self.validator = validator

    @abstractmethod
    def get_institutions(self) -> pd.DataFrame:
        """
        Fetch current list of institutions.
        
        Returns:
            DataFrame with columns:
            - charter_number (str): Unique identifier
            - web_domain (str): Primary web domain
            - city (str): Institution city
            - state (str): Institution state
        """
        pass
    
    @abstractmethod
    def get_quarterly_data(self, date: Optional[datetime] = None) -> pd.DataFrame:
        """
        Fetch quarterly financial data.
        
        Args:
            date: Optional date to fetch historical data
            
        Returns:
            DataFrame with columns:
            - charter_number (str): Unique identifier
            - quarter_end_date (datetime): End of quarter
            - total_assets (float): Total assets in dollars
            - total_deposits (float): Total deposits in dollars
        """
        pass
