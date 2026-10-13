import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

TILT_ADD = 15
VENT_BASE_C = 16
VENT_CM_PER_DEG = 2
VENT_MAX_CM = 20

def sash_plan(sashL, sashW):
    if not (sashL > 0) or not (sashW > 0):
        return {"error": "the sash sides must be positive"}
    area = round1(sashL * sashW)
    if area <= 1: verdict = "a seedling sash"
    elif area <= 2: verdict = "a salad-bed sash"
    else: verdict = "a hot-house sash"
    return {"area": area, "verdict": verdict}

def tilt_plan(latDeg):
    if not (latDeg > 0) or not (latDeg <= 90):
        return {"error": "the latitude must be between 0 and 90"}
    tilt = round1(latDeg + TILT_ADD)
    if tilt <= 45: verdict = "a low tilt"
    elif tilt <= 60: verdict = "a winter tilt"
    else: verdict = "a steep tilt"
    return {"tilt": tilt, "verdict": verdict}

def vent_plan(highC):
    if not (highC > -80):
        return {"error": "the forecast high must be a real temperature"}
    lift = round1(min(VENT_MAX_CM, max(0, (highC - VENT_BASE_C) * VENT_CM_PER_DEG)))
    if lift == 0: verdict = "keep it shut"
    elif lift < VENT_MAX_CM: verdict = "crack it a hand"
    else: verdict = "prop it wide"
    return {"lift": lift, "verdict": verdict}

def render_sash(r, sashL, sashW):
    return "A sash " + fmt(sashL) + " m by " + fmt(sashW) + " m is " + fmt(r["area"]) + " m2 of glazing - " + r["verdict"] + "."

def render_tilt(r, latDeg):
    return ("At a labeled winter rule of latitude plus " + fmt(TILT_ADD) + ", " + fmt(latDeg)
            + " deg asks a sash tilted " + fmt(r["tilt"]) + " deg - " + r["verdict"] + ".")

def render_vent(r, highC):
    if r["lift"] == 0:
        return "A " + fmt(highC) + " C afternoon keeps the lid shut - at or below the labeled " + fmt(VENT_BASE_C) + " C vent rule."
    return "A " + fmt(highC) + " C afternoon asks the lid lifted " + fmt(r["lift"]) + " cm at the prop - " + r["verdict"] + "."

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[1.2,0.8],[1,1],[1.5,1.2],[0.8,0.6],[2,1.5],[1.1,0.9],[2.5,1.5],[0.5,0.5],[0,1],[1.2,0]]:
    add("sashPlan", sash_plan, render_sash, a)
for a in [[52],[30],[40],[45],[20],[60],[35],[48],[0],[95]]:
    add("tiltPlan", tilt_plan, render_tilt, a)
for a in [[22],[14],[30],[16],[18],[26],[10],[24],[-2],[35]]:
    add("ventPlan", vent_plan, render_vent, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
