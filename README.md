# Real-Estate-Price-Prediction
A deep neural net predicting real estate unit prices in Taipei based on traditional data including transactional data and non-traditional data including nearby features and surround map features.
Reached 83% accurarcy with price prediction.

1. Data was cleaned and standardized using the Mean&SD file. Only picked the columns that we felt are important or would contribute to a difference in real estate prices.
2. Data was collected from several geocoding API services: HEREMap for geocoding, Google Map API for nearby search, and Mapbox for map images with corresponding geocodes. The geocoding scripts are for reference. 
3. PLEAE VIEW MODELS IN COLAB. There are several model files to use: for pure csv, for csv+images, and for csv+images but made into a classification model. (For classification, appropriate bins must be created.) 
4. Aggregate all data into one csv file and load the data into a model file.
