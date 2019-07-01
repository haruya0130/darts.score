from flask import Flask, render_template, request
import numpy as np
import json

f = open('arrange.json','r')
json_numbers = json.load(f)
numbers = json_numbers["numbers"]

f = open('count.json','r')
json_counts = json.load(f)
counts = json_counts["counts"]

# 全体で共有する各jsonのidを、jsonに保管しておく
# 追加されるたびに更新する
# id +=1して保存
# destroy/<id> で formからデータのIDを送る
# 

app = Flask(__name__)

@app.route('/')
def main():
    main = ['Arrange','Countup']
    return render_template('main.html', main=main)




@app.route('/player')
def player():
    return render_template('player.html')

@app.route('/Arrange', methods=['GET', 'POST'])
def Arrange():
    json_file = open('arrange.json','r')
    json_numbers = json.load(json_file)
    numbers = json_numbers["numbers"]
    
    if request.method == 'GET':
        return render_template('Arrange.html',numbers=numbers)
    if request.method == 'POST':
        if 'text' in request.form.keys():
            json_file_write = open('arrange.json','w')
            value = request.form['text']
            numbers.append(value)
            
            json_numbers["numbers"] = numbers
            json.dump(json_numbers, json_file_write)
            return render_template('Arrange.html', numbers=numbers)


@app.route('/numbers/destroy/<number>', methods=['POST'])
def destroy_number(number):
    numbers.remove(number)
    # 削除されたnumbersでarrange.jsonを上書き
    f = open('arrange.json','w')
    json_numbers["numbers"] = numbers
    json.dump(json_numbers,f )
    return render_template('Arrange.html', numbers=numbers)

@app.route('/Countup', methods=['GET', 'POST'])
def Countup():
    json_file = open('count.json', 'r')
    json_counts = json.load(json_file)
    counts = json_counts["counts"]
    
    if request.method == 'GET':
        return render_template('countup.html',counts=counts)
    if request.method == 'POST':
        if 'text' in request.form.keys():
            json_file_write = open('count.json', 'w')

            value = request.form['text']
            counts.append(value)
            json_counts["counts"] = counts
            json.dump(json_counts, json_file_write)
            
            return render_template('countup.html',counts=counts)

@app.route('/counts/destroy/<count>', methods=['POST'])
def destroy_count(count):
    counts.remove(count)
    f = open('count.json', 'w')
    json_counts["counts"] = counts
    json.dump(json_counts,f)
    return render_template('countup.html', counts=counts)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=1030)
