# AFAAN OROMOO NEWS CLASSIFICATION SYSTEM

## Overview

AFAAN OROMOO NEWS CLASSIFICATION SYSTEM is a machine learning project designed to classify news articles written in Afaan Oromoo, the Oromo language. The primary goal of this project is to leverage natural language processing (NLP) techniques to automatically categorize news content into various predefined categories.

### Key Features

- **Language Support:** Afaan Oromoo is a widely spoken language, and this project aims to enhance accessibility to news articles in this language.
- **Multiclass Classification:** The system is capable of classifying news articles into multiple categories, providing a comprehensive understanding of the content.
- **Rule-Based Stemmer:** The project incorporates a rule-based stemmer based on the hybrid approach described in the paper "Designing a Stemmer for Afaan Oromo Text: A Hybrid Approach" by Debela Tesfaye.

### Purpose

The motivation behind this project is to contribute to the enhancement of information accessibility for Afaan Oromoo speakers. By automating the categorization of news articles, individuals can easily navigate through relevant content based on their interests.

### Target Audience

This project is intended for individuals interested in Afaan Oromoo language and those seeking to implement or understand machine learning techniques for natural language processing.

## Project Structure

The project is organized into distinct directories, each serving a specific purpose.
📦 my_project
┣ 📂api
┃ ┣ 📜app.py
┃ ┣ 📜model_loader.py
┃ ┗ 📜**init**.py
┣ 📂data
┣ 📂docs
┃ ┣ 📜model_documentation.pdf
┣ 📂logs
┣ 📂models
┃ ┣ 📂trained_models
┃ ┃ ┣ 📜label_encoder.joblib
┃ ┃ ┣ 📜model_20231116_accuracy_0.9263.h5
┃ ┃ ┗ 📜tokenizer.joblib
┃ ┣ 📜train_model.ipynb
┃ ┗ 📜**init**.py
┣ 📂preprocessing
┃ ┣ 📜preprocessing_pipeline.py
┃ ┣ 📜special_character_handler.py
┃ ┣ 📜stemmer.py
┃ ┣ 📜stopword_remover.py
┃ ┣ 📜tokenizer.py
┃ ┗ 📜**init**.py
┣ 📂scrapers
┃ ┣ 📜fbc_scraper.py
┃ ┣ 📜**init**.py
┣ 📂tests
┃ ┣ 📜test_preprocessing.py
┗ 📜requirements.txt

This structure helps maintain code separation and modularity. Key folders include `api` for the Flask API, `preprocessing` for text processing modules, `docs` for documentations, `models` for training and storing trained models, `scrappers` for web scrapping scripts and `tests` for unit tests.

## Getting Started

To set up the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/abdulmunimjemal/afaan-oromoo-news-classification-system.git
   cd afaan-oromoo-news-classification-system
   ```
2. **Install Dependencies:**

```bash
   pip install -r requirements.txt
```

3. **Clone the Repository:**

   ```bash
    cd api
    python app.py
   ```

   The API should now be accessible at http://localhost:5000/predict/.

4. **Test the API:**
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "Your sample afaan oromootext here."}' http://localhost:5000/predict
   ```

Adjust the payload and URL based on your API endpoints.
Now, the project should be set up locally, and you can begin exploring and using the features.

## Dependencies

The project relies on the following external dependencies:

    - **Pandas:**  A powerful data manipulation and analysis library for working with structured data.
    - **Flask:** A lightweight web application framework for the API.
    - **scikit-learn:** A machine learning library for model training and evaluation.
    - **TensorFlow:** An open-source machine learning framework used for building and training neural networks.

    Make sure to install these dependencies using the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Documentation

The project documentation provides detailed information on various aspects of the system. Explore the following sections:

### 1. [Preprocessing Pipeline](./preprocessing/README.md)

This section covers the text preprocessing steps and modules used in the project. Learn how raw text data is transformed and cleaned before being fed into the machine learning model.

### 2. [Model Training](./models/README.md)

Detailed documentation on the process of building, training, and evaluating the machine learning model is available here. Understand the architecture, training approach, and evaluation metrics used in the project.

### 3. [API Usage](./api/README.md)

Explore how to interact with the Flask API and make predictions using the trained machine learning model. The API documentation includes information on endpoints, input requirements, and sample requests.

Refer to each documentation section for in-depth insights into the corresponding components of the project.

## Contributing

We welcome contributions from the community. If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add your feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a pull request

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit [here](https://creativecommons.org/licenses/by-nc-sa/4.0/) or see the `LICENSE.md` file.

**License Summary:** This project is intended for educational and non-commercial purposes only. Users are required to provide proper attribution to the authors and share any derivative works under the same license terms.

## Authors

- Abdulmunim Jundurahman Jemal

## FAQ

### Q: Can I use this project for commercial purposes?

A: No, this project is intended for educational purposes only.

### Q: How do I cite this project?

A: When using this project, please provide proper attribution to the authors.
