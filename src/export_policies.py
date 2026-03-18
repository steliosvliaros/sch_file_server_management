import yaml
from pathlib import Path

master_path = Path('/mnt/data/master_policy.yaml')
out_dir = Path('/mnt/data')

with master_path.open('r', encoding='utf-8') as f:
    master = yaml.safe_load(f)

# Core derived view
core = {
    'schema': {
        'schema_id': 'sch.fileserver.core',
        'schema_version': '3.0.0',
        'status': 'generated',
        'role': 'canonical_identity_and_structure',
        'file_name': 'core_policy.generated.yaml',
        'generated_from': 'master_policy.yaml',
        'do_not_edit': True,
    },
    'policy': {
        'name': master['policy']['name'] + ' - Core View',
        'design_intent': master['policy']['design_intent'],
    },
    'patterns': master['patterns'],
    'constraints': master['constraints'],
    'topology': master['topology'],
    'asset_status_files': master['asset_status_files'],
    'special_asset_folders': master['special_asset_folders'],
    'enums': master['enums'],
    'type_catalog': master['type_catalog'],
    'doc_type_catalog': master['doc_type_catalog'],
    'field_sets': master['field_sets'],
    'master_data_rules': master.get('master_data_rules', {}),
    'filename_rules': master['filename_rules'],
    'workstreams': master['workstreams'],
    'dynamic_selectors': master['dynamic_selectors'],
    'canonical_record_contract': master['canonical_record_contract'],
    'non_goals': master.get('non_goals', []),
}

# Routing derived view
routing = {
    'schema': {
        'schema_id': 'sch.fileserver.routing',
        'schema_version': '3.0.0',
        'status': 'generated',
        'role': 'deterministic_placement_engine',
        'file_name': 'routing_policy.generated.yaml',
        'generated_from': 'master_policy.yaml',
        'do_not_edit': True,
    },
    'depends_on': {
        'master_policy': 'master_policy.yaml'
    },
    'refs': {
        'patterns': 'master_policy.yaml#/patterns',
        'constraints': 'master_policy.yaml#/constraints',
        'enums': 'master_policy.yaml#/enums',
        'doc_type_catalog': 'master_policy.yaml#/doc_type_catalog',
        'field_sets': 'master_policy.yaml#/field_sets',
        'workstreams': 'master_policy.yaml#/workstreams',
        'canonical_record_contract': 'master_policy.yaml#/canonical_record_contract',
    },
    'route_modes': master['route_modes'],
    'route_registry': master['route_registry'],
    'decision_tree': master['decision_tree'],
    'route_output_contract': master['route_output_contract'],
    'confidence_policy': master['confidence_policy'],
    'integrity_checks': master['routing_integrity_checks'],
}

# Governance derived view
governance = {
    'schema': {
        'schema_id': 'sch.fileserver.governance',
        'schema_version': '3.0.0',
        'status': 'generated',
        'role': 'exceptions_validation_and_remediation',
        'file_name': 'governance_policy.generated.yaml',
        'generated_from': 'master_policy.yaml',
        'do_not_edit': True,
    },
    'depends_on': {
        'master_policy': 'master_policy.yaml'
    },
    'refs': {
        'constraints': 'master_policy.yaml#/constraints',
        'special_asset_folders': 'master_policy.yaml#/special_asset_folders',
        'dynamic_selectors': 'master_policy.yaml#/dynamic_selectors',
        'route_output_contract': 'master_policy.yaml#/route_output_contract',
    },
    'exception_classes': master['exception_classes'],
    'archive_rules': master['archive_rules'],
    'normalization_policy': master['normalization_policy'],
    'path_policy': master['path_policy'],
    'review_policy': master['review_policy'],
    'duplicate_keeper_logic': master['duplicate_keeper_logic'],
    'exports_policy': master['exports_policy'],
    'prohibited_patterns': master['prohibited_patterns'],
    'audit_log_contract': master['audit_log_contract'],
    'integrity_checks': master['governance_integrity_checks'],
}

for name, obj in [
    ('core_policy.generated.yaml', core),
    ('routing_policy.generated.yaml', routing),
    ('governance_policy.generated.yaml', governance),
]:
    with (out_dir / name).open('w', encoding='utf-8') as f:
        yaml.safe_dump(obj, f, sort_keys=False, allow_unicode=True, width=1000)

print('Generated core_policy.generated.yaml, routing_policy.generated.yaml, governance_policy.generated.yaml')
