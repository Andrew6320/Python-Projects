RNN-Based Classification with the Poker Hand Dataset

Description:  
In this project, I developed a Python program to train a Recurrent Neural Network (RNN) for classifying poker hands using the Poker Hand dataset. This involved data import and pre-processing, RNN model implementation, and evaluation of model performance through accuracy and confusion matrix analysis.

Key Features:

Dataset Handling:
  - Worked with the Poker Hand dataset, which contains records of poker hands with 10 attributes representing the suit and rank of five cards.
  - Loaded and assigned appropriate column names to both training and testing datasets.

Data Pre-processing:
  - Applied pre-processing by sorting card values and using "StandardScaler" to normalize the data.
  - Reshaped the input data to be suitable for RNN processing.

RNN Model Implementation:
  - Designed a vanilla RNN architecture to model the sequential nature of poker hands.
  - Compiled the model using categorical cross-entropy loss and the Adam optimizer.

Training and Evaluation:
  - Trained the model on the training set and validated its performance using the test set.
  - Evaluated the model’s performance by calculating classification accuracy and generating a confusion matrix.

Performance Insights:
  - Achieved significant accuracy improvements by sorting card values before training.
  - Proposed further enhancements like experimenting with advanced RNN architectures or data augmentation.

Skills Demonstrated:
- proficiency in Python programming and machine learning frameworks like TensorFlow and Keras.
- Experience with RNN design and implementation for sequential data analysis.
- Competence in data pre-processing and transformation techniques.
- Ability to evaluate model performance using metrics such as accuracy and confusion matrix.

