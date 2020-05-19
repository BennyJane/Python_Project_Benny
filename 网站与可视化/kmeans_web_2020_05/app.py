import os
import shutil

from flask import Flask, render_template, request, redirect, url_for

from core.k_means_core import kmeansCore, SEEMethod, drawCategoryPic
from core.dealData import deal, backText, orderDict

app = Flask(__name__)

originDf = deal()
# print(originDf)
k = 3  # 需要进行的聚类类别数
iteration = 500  # 聚类最大循环数


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        action = request.args.get('action')
        if action == 'runSee':
            SEEMethod(originDf, start=1, limit=8)
            seePicPath = '../static/images/see.png'
            return render_template('index.html', all_category=[], all_category_dict={},
                                   seePicPath=seePicPath)
    seePicPath = '../static/images/blank.png'
    return render_template('index.html', all_category=[], all_category_dict={},
                           seePicPath=seePicPath)


@app.route('/category', methods=['Post', 'Get'])
def category():
    if request.method == 'POST':
        k_value = request.form.get('k_value')
        if k_value:
            try:
                k_value = int(k_value)
            except Exception as e:
                seePicPath = '../static/images/blank.png'
                return render_template('index.html', all_category=[], all_category_dict={},
                                       seePicPath=seePicPath)
            resDf = kmeansCore(k_value, iteration, originDf)
            resDf = backText(resDf)
            all_category = resDf['category'].unique().tolist()

            all_category_dict = {}
            for category in all_category:
                tempDf = resDf[resDf['category'] == category]
                tempCategory = tempDf.to_dict(orient='records')
                all_category_dict[category] = tempCategory

            seePicPath = '../static/images/see.png'
            # print(all_category, all_category_dict)
            all_category.sort()

            # 绘制图片
            del_file(r"./static/images/category")
            categoryPicPath = drawCategoryPic(originDf, k_value, resDf)
            print(categoryPicPath)
            return render_template('index.html', all_category=all_category, all_category_dict=all_category_dict,
                                   orderDict=orderDict, categoryPicPath=categoryPicPath,
                                   seePicPath=seePicPath)
    return redirect(url_for('index'))


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

if __name__ == '__main__':
    app.run()
