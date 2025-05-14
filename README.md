# Financial News Sentiment Analysis for Market Prediction

This repository contains all data and code used in the research "Sentiment Analysis in Dutch Financial News: Predicting Market Movements" by Robert Kuipers.

## Overview

This research evaluates the performance of three language models (BERTje, RobBERT, and ChatGPT) in detecting sentiment from Dutch financial news and predicting subsequent stock price movements. The data used for this research includes news articles about companies listed on the AEX, AMX & ASCX, match with the stock price data. The dataset has in total 1470 news events, labeled as:
``Positive'' if AR > 1%
``Negative'' if AR < -1%
``Neutral'' if AR between -1% and 1%

based on the 3-day abnormal return following publication.

## Implementation

The code is written in Python and makes use of transformer-based models for sentiment classification and market prediction. The implementation includes calibrated thresholds for each language model. Performance evaluation metrics and a long-short trading strategy are in the results section. 
