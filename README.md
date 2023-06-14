# chatgpt-sql

The prediction results of ChatGPT on various datasets of Text-to-SQL.

For the specific evaluation methods and results, please refer to this paper "A comprehensive evaluation of ChatGPT's zero-shot Text-to-SQL capability" (https://arxiv.org/pdf/2303.13547.pdf). 

## Download dataset
You can find the datasets in the following links: 
* Spider dataset: https://drive.google.com/uc?export=download&id=1TqleXec_OykOYFREKKtschzY29dUcVAQ
* Spider-SYN dataset: https://github.com/ygan/Spider-Syn
* Spider-DK dataset: https://github.com/ygan/Spider-DK
* Spider-Realistic dataset: https://zenodo.org/record/5205322
* ADVETA: https://github.com/microsoft/ContextualSP
* Spider-CG: https://github.com/ygan/SpiderSS-SpiderCG
* Sparc: https://yale-lily.github.io/sparc
* CoSQL: https://yale-lily.github.io/cosql
* CSPIDER: https://taolusi.github.io/CSpider-explorer/
* DuSQL: https://github.com/luge-ai/luge-ai/tree/master/semantic-parsing

## Test example on spider dataset

### generate data 
```python
python generate_txt.py
```

### generate evaluation result (unzip the database.zip first)
```python
python evaluation.py --gold gold_example.txt --pred pred_example.txt --etype exec --db spider/database --table spider/tables.json
```

The result should be following:

![image](figure/result.png)
