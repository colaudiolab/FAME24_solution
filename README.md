# FAME24_solution
This project is our solution for the FAME challenge at MM 24, which aims to associate voices and faces in a multilingual context.

The complete code is currently being organized and is expected to be released before October 2024.

# Step1 Data prepare
## 1.1 search name through Wiki
The wikipedia has a structure to list all the famous persons, so we utlize this structure to automaticlly download the person names and corresponding image, this step will produce images with person name like `indian_actresses_women/{person_name}.png`

```python
# remember to change the proxy and other parameters in file manually
python craw_wiki_poi.py
```

## 1.2 search youtube videos by names
The code was able to run at Linux a few months ago, but now it seems to be only able to run at Windows.

we will upload these part as soon as possible

## 1.3 Automatically download and process the video data
You can refer to our data sypder project: https://github.com/audio-visual/TalkingVideo 

# Step2 Representation Leanring
we will upload these part as soon as possible

# Step3 FAME V2 training

# Step4 FAME V1 training
