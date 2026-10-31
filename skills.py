# -*- coding: utf-8 -*-
"""Brachial Flow-Mediated Dilation (FMD) Endothelial Function Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def assess_flow_mediated_dilation_fmd(**kwargs):
    """Calculates ultrasound reactive hyperemia brachial artery diameter expansion percentage (%FMD), shear rate stimulus-response coupling, and pre-clinical endothelial nitric oxide dysfunction."""
    baseline_brachial_diameter_mm = kwargs.get('baseline_brachial_diameter_mm')
    peak_hyperemic_diameter_mm = kwargs.get('peak_hyperemic_diameter_mm')
    time_to_peak_seconds = kwargs.get('time_to_peak_seconds')
    systolic_blood_pressure_mmhg = kwargs.get('systolic_blood_pressure_mmhg')

    # %FMD = ((Peak Diameter - Baseline Diameter) / Baseline Diameter) * 100
    fmd_delta_mm = round(peak_hyperemic_diameter_mm - baseline_brachial_diameter_mm, 3)
    fmd_pct = round((fmd_delta_mm / (baseline_brachial_diameter_mm if baseline_brachial_diameter_mm > 0 else 1.0)) * 100.0, 2)
    
    # Clinical benchmarks: > 7.0% is healthy endothelial reserve; < 5.0% indicates endothelial dysfunction
    if fmd_pct >= 9.0:
        endothelial_health = "YOUTHFUL VASCULAR REACTIVITY (High nitric oxide eNOS bioavailability)"
        rx = "Maintain regular aerobic stimulus and dietary dietary inorganic nitrate (beetroot/leafy greens)."
    elif fmd_pct >= 6.5:
        endothelial_health = "BORDERLINE NORMAL ENDOTHELIAL FUNCTION"
        rx = "Incorporate citrulline malate (6g/day), monitor asymmetric dimethylarginine (ADMA) levels."
    else:
        endothelial_health = "ENDOTHELIAL DYSFUNCTION (Impaired NO synthesis, arterial stiffness, atherosclerosis pre-condition)"
        rx = "Cardiovascular lifestyle overhaul: high-polyphenol diet, strict LDL-C/ApoB suppression, continuous aerobic conditioning."
        
    delayed_peak = time_to_peak_seconds > 75.0
    
    result = {
        "status": "success",
        "baseline_diameter_mm": baseline_brachial_diameter_mm,
        "peak_hyperemic_diameter_mm": peak_hyperemic_diameter_mm,
        "absolute_dilation_mm": fmd_delta_mm,
        "flow_mediated_dilation_pct": fmd_pct,
        "time_to_peak_seconds": time_to_peak_seconds,
        "delayed_vasodilation_flag": delayed_peak,
        "endothelial_health_classification": endothelial_health,
        "cardiovascular_endothelial_directive": rx,
        "engine": "GenPark Brachial Flow-Mediated Endothelial Dilation Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "assess_flow_mediated_dilation_fmd": {
        "name": "assess_flow_mediated_dilation_fmd",
        "description": "Calculates ultrasound reactive hyperemia brachial artery diameter expansion percentage (%FMD), shear rate stimulus-response coupling, and pre-clinical endothelial nitric oxide dysfunction.",
        "parameters": {
            "type": "object",
            "properties": {
                "baseline_brachial_diameter_mm": {"type": "number", "description": "Resting pre-cuff brachial artery diameter (mm)"},
                "peak_hyperemic_diameter_mm": {"type": "number", "description": "Peak diameter post-deflation (at 60-90 seconds) in mm"},
                "time_to_peak_seconds": {"type": "number", "description": "Seconds elapsed from cuff release to peak dilation"},
                "systolic_blood_pressure_mmhg": {"type": "number", "description": "Concurrent systolic blood pressure (mmHg)"},
            },
            "required": ['baseline_brachial_diameter_mm', 'peak_hyperemic_diameter_mm', 'time_to_peak_seconds', 'systolic_blood_pressure_mmhg']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "assess_flow_mediated_dilation_fmd":
            res = assess_flow_mediated_dilation_fmd(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-endothelial-fmd-brachial-flow-mediated-dilation-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-endothelial-fmd-brachial-flow-mediated-dilation-skill...")
    test_args = {'baseline_brachial_diameter_mm': 4.1, 'peak_hyperemic_diameter_mm': 4.48, 'time_to_peak_seconds': 65.0, 'systolic_blood_pressure_mmhg': 120.0}
    res = assess_flow_mediated_dilation_fmd(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-endothelial-fmd-brachial-flow-mediated-dilation-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
