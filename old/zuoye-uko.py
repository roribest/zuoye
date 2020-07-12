示例代码（假设本程序和xlsx文件保存在同一目录中，图表存放到 D:\demo\ ）：

import xlwings as xw
import matplotlib.pyplot as plt

# 下面代码从Excel中读取所有数据（包含表头信息）
app = xw.App()
wb = app.books.open('python02_04_01.xlsx')
all_data = wb.sheets(1).range('c3:o12').value
app.quit()

# 设置pyplot的中文兼容性、以及横纵轴标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('月份')
plt.ylabel('产量')

# all_data 中的第一个子列表是表头，
# 其中从第2列开始都是月份名称，对于所有图表都一样，
# 故可以在循环前就一次读出放到变量里随时备用
month_names = all_data[0][1:]

# 从all_data的第二个元素（即产品1）开始逐行读取。
for row in all_data[1:]:
    # 当前子列表row的第一个元素是该行第一列的产品名
    product_name = row[0]
    # 第二个元素开始到最后，是该行各月份产量数据
    counts = row[1:]
    # 以产品名为本图表标题
    plt.title(product_name)
    # 以月份名变量为横轴、产量数据为纵轴绘图
    plt.bar(month_names, counts)
    # 保存图表，以产品名为文件名，png格式
    plt.savefig(f'd:/demo/{product_name}.png')
    # 清空图表以备下次循环绘图    
    plt.clf()
