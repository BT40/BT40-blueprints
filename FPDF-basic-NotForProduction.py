#for python 3 install fpdf package "pip3 install fpdf".

from fpdf import FPDF

#class object FPDF() which is predefiend in side the package fpdf.
document=FPDF(orientation = 'P', unit = 'mm', format='A4')
# pdf = FPDF('P', 'mm', (100, 150)) with custom size

document.set_title("This is custom title")

document.set_margins(25, 20, 20)
# left, top, right...... Define before creating page, otherwise will ruin formatting


#There is no page for the moment, so we have to add one with add_page. 
document.add_page()


#the bottom margin is simply left out of predefinition because it is part of the page break calculation process.
#Therefore, setting a bottom margin in itself is not possible, but it can be done using
#SetAutoPageBreak(boolean auto, [float margin])

#font size setting of the page 
document.set_font("Arial", size=20)

document.set_text_color(255, 255, 255)

document.set_fill_color(20, 50, 80)
# cell fill colour, visible if cell property fill set to true

document.set_draw_color(190, 9, 30)
# border color, used for all drawing operations (lines, rectangles and cell borders)

#txt message  will displayed on pdf page  at the center.
document.cell(w=0, h= 20, txt="This text will appear at top, center aligned", fill=True, ln=1, align="C")
#Align is wrt cell, not page or margins
#ln Indicates where current position should go after call. Possible values are:0- to the right, 1- beginning of next line, 2: below

# Below, we are creating new line and cell with changed colours
document.set_text_color(0, 0, 0)
document.set_fill_color(90, 90, 90)
document.cell(w=0, h=20, txt="This text will appear as Second line", fill=False, border = 1, ln=1, align="L")

#Creating an offset cell
document.cell(40) # Trick for offsetting, create 40mm width empty  cell
document.set_text_color(255, 255, 255)
document.cell(w=0, h= 20, txt="Offsetted Third row,  text center aligned", fill=True, ln=1, align="C")


document.ln(h = 30) #Line break
document.set_text_color(155, 95, 95)
document.multi_cell(w=0, h= 10, border=1, txt="After line break 30mm. This is multi lined \n Line 2 \nLine 3 Justified aligned. This third line is comparatively long. it will automatically insert line break. Lets test it. Hope, it works. Yes it is working ", fill=False, align="J")

#pdf creating.
document.output("file_name.pdf")
   	
print("pdf has been created successfully....")
