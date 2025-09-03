# Movie Recommender System 🎬

A content-based movie recommendation system using TMDB dataset that suggests similar movies based on plot, genres, cast, crew, and keywords.

## 🌟 Features

- Content-based movie recommendations
- Real-time movie poster fetching from TMDB API
- Interactive Streamlit web interface
- Cosine similarity-based movie matching
- Support for 5000+ movies

## 🛠️ Tech Stack

- **Python 3.12**
- **Streamlit** - Web interface
- **scikit-learn** - For content-based filtering
- **pandas** - Data manipulation
- **TMDB API** - Movie data and posters
- **Docker** - Containerization
- **Render** - Deployment

## 🗂️ Project Structure

```
movie_recommender_system/
├── api/
│   └── app.py          # Streamlit web application
├── data/
│   └── raw/            # TMDB movie datasets
├── models/             # Trained model files
├── notebooks/          # Development notebooks
├── docs/              # Documentation
└── tests/             # Test cases
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- TMDB API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Chanukaa2002/Movie-Reccomender-System.git
cd movie_recommender_system
```

2. Create and activate virtual environment:

```bash
python -m venv .venv
# For Windows
.venv\Scripts\activate
# For Linux/Mac
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:

```
TMDB_API_KEY=your_api_key_here
```

5. Run the application:

```bash
streamlit run api/app.py
```

## 🐳 Docker Support

Build and run with Docker:

```bash
docker build -t movie-recommender .
docker run -p 8501:8501 movie-recommender
```

## 🔜 Coming Soon

- Cloud Deployment
- Mobile-responsive UI
- Additional movie metadata
- User ratings integration
- Personalized recommendations

## 🧮 Model Development

The recommendation system uses:

- TF-IDF Vectorization
- Cosine Similarity
- Natural Language Processing for text processing
- Feature extraction from movie metadata

## 📝 License

MIT License

## 👤 Author

Chanuka Dilshan 
