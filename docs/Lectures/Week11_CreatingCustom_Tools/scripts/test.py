import arcpy, os

try:
    outputFC = arcpy.GetParameterAsText(0)
    sr = arcpy.GetParameterAsText(1)
    fClassTemplate = arcpy.GetParameterAsText(2)
    f = open(arcpy.GeoParameterAsText(3), 'r')

    arcpy.CreateFeatureclass_management(os.path.split(outputFC)[0],
                                        os.path.split(outputFC)[1],
                                        "point",
                                        fClassTemplate,
                                        spatial_reference = sr)
    arcpy.Get
    lstFires = f.readlines()
    fields = ["SHAPE@XY", "CONFIDENCEVALUE"]

    with arcpy.da.InsertCursor(outputFC, fields) as cur:
        for fire in lstFires:
            if "Latitude' in Fire:
                continue
            vals = fire.split(",")
            latitude = float(vals[0])
            longitude = float(vals[1])
            confid = int(vals[2])
            row_values [(longitude, latitude), confid]
            cur.insertRow(row_values)
            
except Exception as e:
    print("Error: " + e.args[0])
