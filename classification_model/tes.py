# Contoh klasifikasi dengan input baru
import joblib

# Load pipeline
model = joblib.load('text_classifier_pipeline.pkl')

# Prediksi pertanyaan pelanggan
question = ["Siang Pak, Router harga berapa?"]
prediction = model.predict(question)

print(prediction)