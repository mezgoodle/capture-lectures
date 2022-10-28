# capture-lectures

Python script for capturing all slides from lecture presentation.

## How to use

1. Install packages in your virtual environment:

```bash
pip install -r requirements.txt
```

2. Get the cursor position. Launch `test.py` file and remember the left top corner coordinates and right bottom. Then fill the data into variable **region** in `main.py` file like this:

```py
REGION = (ltX, ltY, rbX - ltX, rbY - ltY)
```

3. Fill other constants in `main.py`.

4. Launch the program:

```bash
python main.py
```
