(function (root) {
  "use strict";
  var TILT_ADD = 15;       // labeled winter rule: sash tilt = latitude + this, deg
  var VENT_BASE_C = 16;    // labeled: keep the lid shut at or below this, C
  var VENT_CM_PER_DEG = 2; // labeled prop lift per degree above base, cm
  var VENT_MAX_CM = 20;    // labeled maximum prop lift, cm

  function round1(x) { return Math.round(x * 10) / 10; }

  function sashPlan(sashL, sashW) {
    if (!(sashL > 0) || !(sashW > 0)) return { error: "the sash sides must be positive" };
    var area = round1(sashL * sashW);
    var verdict;
    if (area <= 1) verdict = "a seedling sash";
    else if (area <= 2) verdict = "a salad-bed sash";
    else verdict = "a hot-house sash";
    return { area: area, verdict: verdict };
  }

  function tiltPlan(latDeg) {
    if (!(latDeg > 0) || !(latDeg <= 90)) return { error: "the latitude must be between 0 and 90" };
    var tilt = round1(latDeg + TILT_ADD);
    var verdict;
    if (tilt <= 45) verdict = "a low tilt";
    else if (tilt <= 60) verdict = "a winter tilt";
    else verdict = "a steep tilt";
    return { tilt: tilt, verdict: verdict };
  }

  function ventPlan(highC) {
    if (!(highC > -80)) return { error: "the forecast high must be a real temperature" };
    var lift = round1(Math.min(VENT_MAX_CM, Math.max(0, (highC - VENT_BASE_C) * VENT_CM_PER_DEG)));
    var verdict;
    if (lift === 0) verdict = "keep it shut";
    else if (lift < VENT_MAX_CM) verdict = "crack it a hand";
    else verdict = "prop it wide";
    return { lift: lift, verdict: verdict };
  }

  function renderSash(r, sashL, sashW) {
    return "A sash " + sashL + " m by " + sashW + " m is " + r.area + " m2 of glazing - " + r.verdict + ".";
  }

  function renderTilt(r, latDeg) {
    return "At a labeled winter rule of latitude plus " + TILT_ADD + ", " + latDeg
      + " deg asks a sash tilted " + r.tilt + " deg - " + r.verdict + ".";
  }

  function renderVent(r, highC) {
    if (r.lift === 0) return "A " + highC + " C afternoon keeps the lid shut - at or below the labeled " + VENT_BASE_C + " C vent rule.";
    return "A " + highC + " C afternoon asks the lid lifted " + r.lift + " cm at the prop - " + r.verdict + ".";
  }

  var api = { sashPlan: sashPlan, tiltPlan: tiltPlan, ventPlan: ventPlan, renderSash: renderSash, renderTilt: renderTilt, renderVent: renderVent };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.ColdFrameMath = api;
})(this);
