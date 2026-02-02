#!/bin/bash

# 1. Sanal ortamı aktif et (Windows terminal yapısına uygun yol)
# Not: Git Bash üzerinde çalıştırıyorsan bu yol geçerlidir.
source .venv/Scripts/activate

# 2. Testleri çalıştır
pytest data/test_app.py

# 3. Pytest'in çıkış kodunu yakala
# $? değişkeni bir önceki komutun (pytest) sonucunu tutar.
TEST_RESULT=$?

# 4. Sonuca göre exit code döndür
if [ $TEST_RESULT -eq 0 ]; then
    echo "Tebrikler! Tüm testler başarıyla geçti."
    exit 0
else
    echo "Hata! Bazı testler başarısız oldu."
    exit 1
fi