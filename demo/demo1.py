from lxml import etree, html
import csv

parser = etree.HTMLParser()
tree = etree.parse("demo.html", parser)

data = tree.xpath('//*[@id="foreignTable"]//text()')

data = [data[i:i + 5] for i in range(0, len(data), 5)]

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    print('helloworld')    
    writer.writerows(data)
