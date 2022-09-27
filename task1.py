def ptotal (molar1, molar2, mass1, mass2, temper, ob):
temper2 = 273.15 + temper
    first_solv = (molar1/mass1 + molar2/ mass2) * temper2 * 0.082 
    return first_solv/ob
