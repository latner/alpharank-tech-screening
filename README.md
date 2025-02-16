# AlphaRank Tech Screening / Code Challenge

A data pipeline for analyzing bank and credit union financial data from FDIC and NCUA sources.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install package with development dependencies:
```bash
pip install -e ".[dev]"
```

## Project Structure

- `src/alpharank/`: Main package directory
  - `sources/`: Data source implementations
  - `storage/`: Data storage implementations
  - `analysis/`: Analysis and query tools
- `tests/`: Test directory
- `notebooks/`: Jupyter notebooks
- `docs/`: Documentation

## Development

1. Run tests:
```bash
pytest
```

2. Format code:
```bash
black src tests
```

3. Type checking:
```bash
mypy src
```

## License
(Probably a good idea.)
