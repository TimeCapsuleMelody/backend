FROM python:3.10

# 작업 디렉토리를 /app/src로 설정
WORKDIR /app/src

# requirements.txt 파일을 /app 디렉토리로 복사
COPY requirements.txt /app/

# 의존성 설치
RUN pip install --no-cache-dir -r /app/requirements.txt

# src 폴더의 내용을 /app/src로 복사
COPY src/ .

# 필요한 경우 상위 디렉토리의 다른 파일들도 복사
# 예: COPY config.py /app/

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]