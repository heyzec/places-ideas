from openlocationcode import openlocationcode as olc

def plus_code_to_coord(plus_code):
    """Only converts Singapore plus codes to coordinates."""
    SG_LAT = 1.290270
    SG_LONG = 103.851959

    assert plus_code.split(' ')[1] == 'Singapore'
    short_code = plus_code.split(' ')[0]
    full_code = olc.recoverNearest(short_code, SG_LAT, SG_LONG)
    results = olc.decode(full_code)
    lat, long = results.latitudeCenter, results.longitudeCenter
    return lat, long
