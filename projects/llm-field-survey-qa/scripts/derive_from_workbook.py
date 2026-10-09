"""Create public-safe QA summaries from the de-identified AGV survey workbook.

The script intentionally keeps only generalized engineering concepts. It does
not copy customer, project, person, exact site, network, or system values.
"""
import argparse, json
from pathlib import Path

PUBLIC_ROWS = [
    ("workbook_001", "site_scenario", "在开始 AGV 工勘时，为什么要先记录作业场景、班次和环境条件？", "这些信息决定设备的运行时间、负载变化、温度范围和现场作业方式，是后续判断定位、通信、续航和安全要求的基础。"),
    ("workbook_002", "floor_and_route", "工勘中为什么要记录地面材质、接缝、坡度和转弯空间？", "地面和路线条件会影响驱动打滑、定位稳定性、通过性和制动距离。应把这些条件与 AGV 的尺寸、最小转弯半径和运行速度一起评估。"),
    ("workbook_003", "load_interface", "货架或工装对接前需要确认哪些尺寸？", "需要确认外形尺寸、底部净空、对接高度、允许误差、进出方向和 AGV 原地转向所需空间，并把测量值与设备能力逐项核对。"),
    ("workbook_004", "cellular_network", "5G 网络工勘不能只看信号强度，还要检查什么？", "还要检查 AGV 运行轨迹上的信号质量、干扰、吞吐、切换行为、平均时延和连续丢包情况，并用持续运行测试验证结果。"),
    ("workbook_005", "wifi_network", "Wi-Fi 工勘需要验证哪些条件？", "需要确认运行区域连续覆盖、接入点漫游能力、信道干扰、专用网络隔离、设备接入容量和持续 ping 测试结果。"),
    ("workbook_006", "system_integration", "为什么要在工勘阶段确认 WMS、MES、PLC 或 WCS 的接口边界？", "因为任务下发、库位状态、呼叫、设备状态和异常处理可能分属不同系统。接口边界不清楚，现场测试时很难判断问题来自机器人、调度系统还是上位系统。"),
    ("workbook_007", "safety", "现场安全工勘中为什么要单独记录人员、消防设施和障碍物？", "这些因素会改变路线可行性、感知范围和安全停车条件。需要确认人车关系、固定设施位置、低矮或高空障碍物以及不可检测区域。"),
    ("workbook_008", "evidence_collection", "工勘表中的现场照片、视频和网络测试结果有什么作用？", "它们把口头描述变成可以复核的证据，便于设计路线、定位风险、复现问题，并在交付前后检查同一项要求是否已经满足。"),
    ("workbook_009", "follow_up", "工勘结论为什么要同时记录待办事项、状态和责任人？", "这样可以把发现的问题转成可跟踪的工程任务，明确谁负责补充数据、修改现场条件或重新测试，避免风险只停留在会议记录里。"),
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="local de-identified workbook; used only to verify it can be opened")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    try:
        from openpyxl import load_workbook
        wb = load_workbook(args.input, read_only=True, data_only=True)
        sheet_count = len(wb.sheetnames)
        row_count = sum(ws.max_row for ws in wb.worksheets)
    except ImportError as exc:
        raise SystemExit("Install openpyxl to import an .xlsx workbook: " + str(exc))
    out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for rid, category, question, answer in PUBLIC_ROWS:
            f.write(json.dumps({"id": rid, "category": category, "question": question, "answer": answer, "source_type": "user_provided_deidentified_workbook", "public_safe_summary": True}, ensure_ascii=False) + "\n")
    print(json.dumps({"sheets_read": sheet_count, "rows_read": row_count, "records_written": len(PUBLIC_ROWS), "output": str(out), "copied_raw_values": False}, ensure_ascii=False))

if __name__ == "__main__":
    main()
