FROM nvcr.io/nvidia/tensorflow:21.09-tf2-py3
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install tensorflow-datasets matplotlib pandas segmentation-models scikit-learn patchify opencv-python

WORKDIR /app

ENTRYPOINT [ "jupyter", "notebook" ]