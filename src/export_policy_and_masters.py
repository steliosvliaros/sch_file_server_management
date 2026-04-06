#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


@dataclass
class CompanyRecord:
    company_id: str
    display_name: str
    absolute_company_root_path: str
    namecode: str
    typ3: str
    vat9: str
    company_folder: str
    is_active: bool = True
    notes: str = ""


@dataclass
class AssetRecord:
    asset_id: str
    company_id: str
    company_folder: str
    absolute_company_root_path: str
    type: str
    metric: str
    ss: str
    typeid: str
    project_name: str
    location: str
    asset_folder: str
    lifecycle_status: str = "active"
    is_active: bool = True
    notes: str = ""


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("Master policy YAML must load as a mapping.")
    return data


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def ensure_str(value: Any) -> str:
    return "" if value is None else str(value)


def split_typeid(typeid: str) -> tuple[str, str, str]:
    typeid = ensure_str(typeid)
    if len(typeid) < 6 or "-" not in typeid:
        return "", "", ""
    prefix, ss = typeid.rsplit("-", 1)
    return prefix[:3], prefix[3:], ss


def build_company_folder(namecode: str, typ3: str, vat9: str) -> str:
    return f"{namecode}-{typ3}-{vat9}"


def build_typeid(type_code: str, metric: str, ss: str) -> str:
    return f"{type_code}{metric}-{ss}"


def build_asset_folder(typeid: str, project_name: str, location: str) -> str:
    return f"{typeid}_{project_name}_{location}"


def build_folder_index(master: Dict[str, Any]) -> Dict[str, str]:
    folder_index: Dict[str, str] = {}
    workstreams = master.get("workstreams", {})
    for ws in workstreams.values():
        root = ws.get("root_folder") or {}
        misc = ws.get("misc_review_folder") or {}
        if root.get("id") and root.get("name"):
            folder_index[root["id"]] = root["name"]
        if root.get("name") and misc.get("id") and misc.get("name"):
            folder_index[misc["id"]] = f"{root['name']}/{misc['name']}"
        for sub in (ws.get("subfolders") or {}).values():
            if root.get("name") and sub.get("id") and sub.get("name"):
                folder_index[sub["id"]] = f"{root['name']}/{sub['name']}"
    for special in (master.get("special_asset_folders") or {}).values():
        if special.get("id") and special.get("name"):
            folder_index[special["id"]] = special["name"]
    return folder_index


def build_policy_json(master: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "schema": {
            "schema_id": "sch.fileserver.policy_json",
            "schema_version": "1.0.0",
            "generated_from": ensure_str(master.get("schema", {}).get("file_name", "master_policy.yaml")),
            "generated_at": now_iso(),
        },
        "policy": {
            "name": master.get("policy", {}).get("name", "SCH Policy"),
            "design_intent": master.get("policy", {}).get("design_intent", []),
        },
        "core": {
            "patterns": master.get("patterns", {}),
            "constraints": master.get("constraints", {}),
            "asset_status_files": master.get("asset_status_files", []),
            "topology": master.get("topology", {}),
            "special_asset_folders": master.get("special_asset_folders", {}),
            "enums": master.get("enums", {}),
            "type_catalog": master.get("type_catalog", {}),
            "doc_type_catalog": master.get("doc_type_catalog", {}),
            "field_sets": master.get("field_sets", {}),
            "filename_rules": master.get("filename_rules", {}),
            "workstreams": master.get("workstreams", {}),
            "canonical_record_contract": master.get("canonical_record_contract", {}),
            "folder_index": build_folder_index(master),
        },
        "routing": {
            "route_modes": master.get("route_modes", {}),
            "route_registry": master.get("route_registry", {}),
            "decision_tree": master.get("decision_tree", []),
            "route_output_contract": master.get("route_output_contract", {}),
            "confidence_policy": master.get("confidence_policy", {}),
            "integrity_checks": master.get("routing_integrity_checks", master.get("integrity_checks", [])),
        },
        "governance": {
            "exception_classes": master.get("exception_classes", {}),
            "archive_rules": master.get("archive_rules", {}),
            "normalization_policy": master.get("normalization_policy", {}),
            "path_policy": master.get("path_policy", {}),
            "review_policy": master.get("review_policy", {}),
            "duplicate_keeper_logic": master.get("duplicate_keeper_logic", {}),
            "exports_policy": master.get("exports_policy", {}),
            "prohibited_patterns": master.get("prohibited_patterns", []),
            "audit_log_contract": master.get("audit_log_contract", {}),
        },
    }


def normalize_company_records(raw_companies: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for idx, raw in enumerate(raw_companies, start=1):
        namecode = ensure_str(raw.get("namecode") or raw.get("NAMECODE")).strip()
        typ3 = ensure_str(raw.get("typ3") or raw.get("TYP3")).strip()
        vat9 = ensure_str(raw.get("vat9") or raw.get("VAT9")).strip()
        display_name = ensure_str(raw.get("display_name") or raw.get("name") or raw.get("company_name")).strip()
        company_folder = ensure_str(raw.get("company_folder")).strip() or build_company_folder(namecode, typ3, vat9)
        company_id = ensure_str(raw.get("company_id")).strip() or f"CMP-{idx:04d}"
        absolute_company_root_path = ensure_str(raw.get("absolute_company_root_path") or raw.get("company_root_path")).strip()
        record = CompanyRecord(
            company_id=company_id,
            display_name=display_name or namecode or company_folder,
            absolute_company_root_path=absolute_company_root_path,
            namecode=namecode,
            typ3=typ3,
            vat9=vat9,
            company_folder=company_folder,
            is_active=bool(raw.get("is_active", True)),
            notes=ensure_str(raw.get("notes", "")),
        )
        records.append(record.__dict__)
    return records


def derive_companies_from_assets(raw_assets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: Dict[str, Dict[str, Any]] = {}
    for raw in raw_assets:
        company_folder = ensure_str(raw.get("company_folder")).strip()
        if not company_folder:
            continue
        company_id = ensure_str(raw.get("company_id")).strip() or company_folder
        if company_id in seen:
            continue
        parts = company_folder.split("-")
        namecode = parts[0] if len(parts) >= 3 else ""
        typ3 = parts[-2] if len(parts) >= 3 else ""
        vat9 = parts[-1] if len(parts) >= 3 else ""
        seen[company_id] = CompanyRecord(
            company_id=company_id,
            display_name=namecode or company_folder,
            absolute_company_root_path=ensure_str(raw.get("absolute_company_root_path") or raw.get("company_root_path")),
            namecode=namecode,
            typ3=typ3,
            vat9=vat9,
            company_folder=company_folder,
        ).__dict__
    return list(seen.values())


def build_company_master(master: Dict[str, Any]) -> Dict[str, Any]:
    master_data = master.get("master_data", {}) or {}
    raw_companies = master_data.get("companies") or master.get("companies") or []
    raw_assets = master_data.get("assets") or master.get("assets") or []
    companies = normalize_company_records(raw_companies) if raw_companies else derive_companies_from_assets(raw_assets)
    return {
        "schema": {
            "schema_id": "sch.fileserver.company_master",
            "schema_version": "1.0.0",
            "generated_from": ensure_str(master.get("schema", {}).get("file_name", "master_policy.yaml")),
            "generated_at": now_iso(),
        },
        "fields": {
            "company_id": "Stable internal company record id",
            "display_name": "Human-friendly company name",
            "absolute_company_root_path": "Required absolute base path for this company on the local file system",
            "namecode": "Short code used in company folder naming",
            "typ3": "3-letter legal type",
            "vat9": "9-digit VAT",
            "company_folder": "Canonical company root folder name",
            "is_active": "Whether company is active for new filing",
            "notes": "Free notes",
        },
        "companies": companies,
    }


def normalize_asset_records(raw_assets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    for idx, raw in enumerate(raw_assets, start=1):
        company_id = ensure_str(raw.get("company_id")).strip()
        company_folder = ensure_str(raw.get("company_folder")).strip()
        typeid = ensure_str(raw.get("typeid") or raw.get("TYPEID")).strip()
        type_code = ensure_str(raw.get("type") or raw.get("TYPE")).strip()
        metric = ensure_str(raw.get("metric") or raw.get("METRIC")).strip()
        ss = ensure_str(raw.get("ss") or raw.get("SS")).strip()
        if typeid and (not type_code or not metric or not ss):
            t, m, s = split_typeid(typeid)
            type_code = type_code or t
            metric = metric or m
            ss = ss or s
        if not typeid and type_code and metric and ss:
            typeid = build_typeid(type_code, metric, ss)
        project_name = ensure_str(raw.get("project_name") or raw.get("PROJECT_NAME")).strip()
        location = ensure_str(raw.get("location") or raw.get("LOCATION")).strip()
        asset_folder = ensure_str(raw.get("asset_folder") or raw.get("ASSET_FOLDER")).strip()
        if not asset_folder and typeid and project_name and location:
            asset_folder = build_asset_folder(typeid, project_name, location)
        asset_id = ensure_str(raw.get("asset_id")).strip() or f"AST-{idx:05d}"
        record = AssetRecord(
            asset_id=asset_id,
            company_id=company_id,
            company_folder=company_folder,
            type=type_code,
            metric=metric,
            ss=ss,
            typeid=typeid,
            project_name=project_name,
            location=location,
            asset_folder=asset_folder,
            lifecycle_status=ensure_str(raw.get("lifecycle_status", "active")),
            is_active=bool(raw.get("is_active", True)),
            notes=ensure_str(raw.get("notes", "")),
        )
        records.append(record.__dict__)
    return records


def build_assets_master(master: Dict[str, Any]) -> Dict[str, Any]:
    master_data = master.get("master_data", {}) or {}
    raw_assets = master_data.get("assets") or master.get("assets") or []
    assets = normalize_asset_records(raw_assets)
    return {
        "schema": {
            "schema_id": "sch.fileserver.assets_master",
            "schema_version": "1.0.0",
            "generated_from": ensure_str(master.get("schema", {}).get("file_name", "master_policy.yaml")),
            "generated_at": now_iso(),
        },
        "fields": {
            "asset_id": "Stable internal asset record id",
            "company_id": "Foreign key to company_master.company_id",
            "company_folder": "Canonical company root folder name",
            "absolute_company_root_path": "Inherited from company master for full path validation",
            "type": "3-letter project type",
            "metric": "Encoded metric portion of TYPEID",
            "ss": "2-digit collision sequence",
            "typeid": "Canonical TYPEID",
            "project_name": "Project name used in asset folder",
            "location": "Location used in asset folder",
            "asset_folder": "Canonical asset folder name",
            "lifecycle_status": "Asset lifecycle state",
            "is_active": "Whether asset is active for new filing",
            "notes": "Free notes",
        },
        "assets": assets,
    }


def build_asset_types(master: Dict[str, Any]) -> Dict[str, Any]:
    type_catalog = master.get("type_catalog", {}) or {}
    base_unit_multipliers = {
        "MW": {"display_unit": "MW", "base_value_unit": "kW", "input_to_base_multiplier": {"MW": 1000, "kW": 1, "kWp": 1}},
        "m2": {"display_unit": "m2", "base_value_unit": "m2", "input_to_base_multiplier": {"m2": 1, "ha": 10000}},
        "tpy": {"display_unit": "tpy", "base_value_unit": "tpy", "input_to_base_multiplier": {"tpy": 1}},
        "beds": {"display_unit": "beds", "base_value_unit": "beds", "input_to_base_multiplier": {"beds": 1}},
        "kg_day": {"display_unit": "kg/day", "base_value_unit": "kg/day", "input_to_base_multiplier": {"kg/day": 1}},
        "kWh": {"display_unit": "kWh", "base_value_unit": "kWh", "input_to_base_multiplier": {"MWh": 1000, "kWh": 1}},
        "unit": {"display_unit": "unit", "base_value_unit": "unit", "input_to_base_multiplier": {"unit": 1}},
    }
    type_rows: List[Dict[str, Any]] = []
    for type_code, entry in type_catalog.items():
        base_unit = ensure_str(entry.get("base_unit"))
        allowed_input_units = entry.get("allowed_input_units", [])
        unit_config = base_unit_multipliers.get(base_unit, {
            "display_unit": base_unit,
            "base_value_unit": base_unit,
            "input_to_base_multiplier": {unit: 1 for unit in (allowed_input_units or [base_unit])},
        })
        input_to_base_multiplier = {
            unit: factor
            for unit, factor in unit_config["input_to_base_multiplier"].items()
            if unit in allowed_input_units
        }
        metric_rule = f"Convert input to integer {unit_config['base_value_unit']}, then metric = total//1000 as XX and total%1000 as YYY."
        type_rows.append({
            "type_code": type_code,
            "label": ensure_str(entry.get("label")),
            "characteristic": ensure_str(entry.get("characteristic")),
            "display_unit": unit_config["display_unit"],
            "base_value_unit": unit_config["base_value_unit"],
            "allowed_input_units": allowed_input_units,
            "input_to_base_multiplier": input_to_base_multiplier,
            "metric_rule": metric_rule,
            "example": ensure_str(entry.get("example")),
        })
    return {
        "schema": {
            "schema_id": "sch.fileserver.asset_types",
            "schema_version": "1.0.0",
            "generated_from": ensure_str(master.get("schema", {}).get("file_name", "master_policy.yaml")),
            "generated_at": now_iso(),
        },
        "asset_types": type_rows,
    }


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def has_embedded_master_records(master: Dict[str, Any]) -> bool:
    master_data = master.get("master_data", {}) or {}
    return bool(
        master_data.get("companies")
        or master_data.get("assets")
        or master.get("companies")
        or master.get("assets")
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Export policy JSON, asset types, company master, and assets master from master_policy.yaml")
    parser.add_argument("master", nargs="?", default="/mnt/data/master_policy.yaml", help="Path to master_policy.yaml")
    parser.add_argument("--out-dir", default="/mnt/data", help="Output directory for JSON files")
    parser.add_argument("--policy-name", default="policy.json", help="Output filename for policy JSON")
    parser.add_argument("--asset-types-name", default="asset_types.json", help="Output filename for asset types JSON")
    parser.add_argument("--company-name", default="company_master.json", help="Output filename for company master JSON")
    parser.add_argument("--assets-name", default="assets_master.json", help="Output filename for assets master JSON")
    args = parser.parse_args()

    master_path = Path(args.master)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    master = load_yaml(master_path)
    write_json(out_dir / args.policy_name, build_policy_json(master))
    write_json(out_dir / args.asset_types_name, build_asset_types(master))
    wrote_company = False
    wrote_assets = False
    if has_embedded_master_records(master):
        write_json(out_dir / args.company_name, build_company_master(master))
        write_json(out_dir / args.assets_name, build_assets_master(master))
        wrote_company = True
        wrote_assets = True

    print(f"Wrote {out_dir / args.policy_name}")
    print(f"Wrote {out_dir / args.asset_types_name}")
    if wrote_company:
        print(f"Wrote {out_dir / args.company_name}")
    else:
        print(f"Skipped {out_dir / args.company_name} (no embedded company data in master policy)")
    if wrote_assets:
        print(f"Wrote {out_dir / args.assets_name}")
    else:
        print(f"Skipped {out_dir / args.assets_name} (no embedded asset data in master policy)")


if __name__ == "__main__":
    main()
