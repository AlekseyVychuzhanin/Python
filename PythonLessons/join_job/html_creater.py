from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(device = 1):
    style = 'style="font-size:22px"'
    html = '<html>\n <head><head>\n <body>\n'
    html += '   <p {}>temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}>pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   <p {}>wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    
    with open('index.html', 'w') as page:
        page.write(html)
    
    return html

def new_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:22px"'
    html = '<html>\n <head><head>\n <body>\n'
    html += '   <p {}>temperature: {} c</p>\n'\
        .format(style, t)
    html += '   <p {}>pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '   <p {}>wind_speed: {} m/s</p>\n'\
        .format(style, w)
    
    with open('new_index.html', 'w') as page:
        page.write(html)
    
    return data