import baseTypes as bt

window = bt.window(drawOnUpdate=False)

circle = window.create_circle("#",(20,10),7,color="f_Red")
window._rem(circle)
window.draw()