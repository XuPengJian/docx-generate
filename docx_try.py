from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm

doc = DocxTemplate("my_word_template.docx")
# # 插入图片
# image_placeholder = doc.find("{{image_placeholder}}")
image_path = "F:/jupyter/cn_ocr/text.png"
# 创建图片对象
# insert_image1 = InlineImage(doc, image_path, width=Mm(408), height=Mm(341))
# # 插入图片到指定位置
# doc.insert_image(image_placeholder, image_path)
context = {'company_name': "World company",
           'image_placeholder': InlineImage(doc, image_path, width=Mm(24), height=Mm(20)),
           'test_data': [
               {
                   'num': 99,
                   'grade': 'A',
               },
               {
                   'num': 95,
                   'grade': 'B',
               },
           ]}
doc.render(context)
doc.save("generated_doc.docx")