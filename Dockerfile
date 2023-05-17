FROM gcr.io/tfx-oss-public/tfx:1.13.0

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ src/

ENV PYTHONPATH="/pipeline:${PYTHONPATH}"
