from user_inteface import temperature_view
from user_inteface import wind_speed_view
from user_inteface import preassure_view


def create(device=1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}<temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}<wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '    <preassure_view units = "mmHg">{}<temperature>\n'\
        .format(preassure_view(device))
    xml += '</html>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml


def new_create(data, device=1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '    <temperature units = "f">{}<temperature>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/s">{}<wind_speed_view>\n'\
        .format(p)
    xml += '    <preassure_view units = "mmHg">{}<temperature>\n'\
        .format(w)
    xml += '</html>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data
