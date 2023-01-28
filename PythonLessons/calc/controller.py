import model_mult as model
import view

def button_click():
    volue_a = view.get_value()
    volue_b = view.get_value()
    model.init(volue_a, volue_b)
    result = model.do_it()
    view.view_data(result, 'result')