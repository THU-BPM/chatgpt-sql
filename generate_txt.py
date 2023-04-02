import json

with open('spider/predict.json', 'r') as f:
    data = json.load(f)

gold_result = open('gold_example.txt', 'w')
pred_result = open('pred_example.txt', 'w')

for item in data:
    gold_result.write(item['query'] + '\t' + item['db_id'] + '\n')
    result_query = 'SELECT ' + item['result'].replace('\n', ' ')
    result_query = result_query.replace('SELECT SELECT', 'SELECT')
    pred_result.write(result_query + '\n')
