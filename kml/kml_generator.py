import pandas as pd

from lxml import etree
from pykml.factory import KML_ElementMaker as KML


def generate_kml():
    base_path = "data/places.xlsx"
    df = pd.read_excel(base_path, 'Sheet1')
    print(df)

    placemarks = []

    for index, row in df.iterrows():
        # KML format is (long, lat) instead of the traditional (lat, long)
        coordinates = row["coordinates"].split(",")
        xy = f"{coordinates[1]},{coordinates[0]}"
        
        description = f"""Places: {row["area"]}
Reason: {row["subtype"]}
Source: {row["source"]}
Date added: {row["date_added"]}
GMaps: {row["gmaps"]}

Comments:
{row["comments"]}"""
        description = '<br>\n'.join(description.splitlines())

        pm = KML.Placemark(
            KML.name(row["name"]),
            KML.Point(
                KML.coordinates(xy)
            ),
            KML.description(description)
        )
        placemarks.append(pm)

    doc = KML.Document(
            KML.name("My layer"),
            *placemarks
    )
    output = etree.tostring(doc, pretty_print=True).decode()
    return output

    # with open("out.kml", 'wt') as f:
    #     f.write(output)
