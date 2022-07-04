import json
  

f = open('data.json')
  

data = json.load(f)

pip3 install googletrans

from googletrans import Translator, constants
from pprint import pprint

translator = Translator()
  
translation1 = translator.translate("My country’s name is Bangladesh. Bangladesh is a very small country huge population. It is a medium-developed country in South Asia. We 
		  have a very good and progressing economy. It has an area of 147,570 square kilometers. But it has a population of 164 million. That is huge 		  than the area.", dest="ba")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

translation2 = translator.translate("My country’s name is Bangladesh. Bangladesh is a very small country huge population. It is a medium-developed country in South Asia. We 
		  have a very good and progressing economy. It has an area of 147,570 square kilometers. But it has a population of 164 million. That is huge 		  than the area.", dest="hi")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

translation3 = translator.translate("My country’s name is Bangladesh. Bangladesh is a very small country huge population. It is a medium-developed country in South Asia. We 
		  have a very good and progressing economy. It has an area of 147,570 square kilometers. But it has a population of 164 million. That is huge 		  than the area.", dest="ch")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

translation4 = translator.translate("My country’s name is Bangladesh. Bangladesh is a very small country huge population. It is a medium-developed country in South Asia. We 
		  have a very good and progressing economy. It has an area of 147,570 square kilometers. But it has a population of 164 million. That is huge 		  than the area.", dest="ja")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 15)

pdf.cell(200, 10, txt = "Translation",
         ln = 1, align = 'C')

pdf.cell(200, 10, txt = translation1,
         ln = 2, align = 'C')

pdf.cell(200, 10, txt = translation2,
         ln = 2, align = 'C')

pdf.cell(200, 10, txt = translation3,
         ln = 2, align = 'C')

pdf.cell(200, 10, txt = translation4,
         ln = 2, align = 'C')

pdf.output("testExpo.pdf") 

 
f.close()