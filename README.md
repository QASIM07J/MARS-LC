# Mars Landform Classification

Streamlit app for classifying Mars surface landforms from uploaded images using trained PyTorch models.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this project to a GitHub repository under `QASIM07J`.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Create a new app from the repository.
4. Set the main file path to `app.py`.
5. Deploy.

The largest model file is under GitHub's 100 MB file limit. If GitHub rejects a model file, move the `.pth` files to Git LFS or external storage and update `utils/model_utils.py` to download/load them.
