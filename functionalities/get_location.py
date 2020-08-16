import geocoder
import reverse_geocoder as rg

def get_current_location():
    g = geocoder.ip('me')
    result = rg.search(g.latlng)
    
    return result[0]['name']