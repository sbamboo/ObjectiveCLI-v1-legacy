import baseTypes as bt

import os; os.system("")

window = bt.window(drawOnUpdate=False)

window.clear()
circle = window.create_circle("#",(20,10),7,color="f_Red")
window.draw()
window.sleep(0.5)
window.moveto(circle,(20,20))
window.draw()
window.sleep(0.5)
point = window.create_point("#",(10,10),color="f_Blue")
window.draw()
window.sleep(0.5)
line = window.create_line("#",(7,7),(30,10),color="f_Magenta")
window.draw()