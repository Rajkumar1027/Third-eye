import cv2
import numpy
import ultralytics
import torch
import transformers
import pyttsx3
import speech_recognition
import pyaudio
import pygame
import pytesseract
import easyocr
import requests
import dotenv

print("✅ All libraries imported successfully!")
print(f"PyTorch CUDA available: {torch.cuda.is_available()}")
print(f"OpenCV version: {cv2.__version__}")