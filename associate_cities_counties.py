# Iterate over cities and, for each, look up the appropriate county and adjust
# the association.

def run(apps=None):
    if apps:
        City = apps.get_model("locations", "City")
        County = apps.get_model("locations", "County")
    else:
        from frontend.apps.locations.models import (City, County)

    for c in City.objects.all():
        try:
            # Look up county with existing county name but state from city
            n = c.county.name
            s = c.state
            c.county = County.objects.get(name=n, state=s)
            c.save()
        except:
            pass
