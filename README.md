# Introduction to Artificial Intelligence

This repository contains my projects from the **Introduction to Artificial Intelligence** course at the **University of South Florida**, taught by Professor **John Licato**.
The projects cover foundational AI concepts, algorithms, and real-world problem-solving techniques.

## Course Overview

Throughout this course, I implemented and tested algorithms in search, optimization, machine learning, and reasoning.
The work demonstrates both theoretical understanding and practical coding skills.

## Projects

### 1. The Tile Sliding Game | A* Search

Solved the classic tile sliding puzzle using the A\* search algorithm with the Manhattan distance heuristic.
Found the optimal sequence of moves to solve an nxn sliding puzzle.

### 2. 3D Tic Tac Toe | Alpha-beta with Forward Pruning

It is a competitive 3D Tic Tac Toe AI using alpha-beta forward pruning for move selection.
Implemented two different heuristics, set them to play against each other, and analyzed game outcomes to evaluate heuristic effectiveness.

### 3. Sentiment Analysis 

Implemented a sentiment analysis model that trains on a JSON dataset of labeled reviews to determine whether new text is positive or negative.
Removed extreme values using percentile thresholds and normalized sentiment scores to -1, 0, or 1 for classification.

### 4. ModernBERT NLI | Natural Language Inference

Fine-tuned a ModernBERT model on the AllNLI dataset to classify entailment, contradiction, and neutral sentence pairs.
Evaluated performance using F1 score, confusion matrices, and manual test cases to identify model weaknesses and class imbalances.
Analyzed true/false positive and negative rates to validate hypotheses about prediction errors in test cases.

## Tools

- **Languages:** Python
- **Libraries:** NLTK, NumPy, PyTorch, Hugging Face Transformers, scikit-learn
- **Other:** Jupyter Notebook, Google Colab