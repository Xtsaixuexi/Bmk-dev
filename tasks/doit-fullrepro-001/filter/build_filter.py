from pathlib import Path
import ast, json, re, csv
TASK=Path('/root/autodl-tmp/Bmk-Lizhiqian/wip/doit-fullrepro-001')
SRC=Path('/root/autodl-tmp/new-e2e/pydoit__doit')
FILTER=TASK/'filter'
nodeids=[]
for line in (FILTER/'collected_nodeids.txt').read_text().splitlines():
    line=line.strip()
    if '::' not in line or line.startswith('=') or line.startswith('/') or line.startswith('--'):
        continue
    # include collected helper artifacts too; normalize to repo-root nodeids
    if not line.startswith('tests/'):
        line='tests/'+line
    if (SRC/line.split('::')[0]).exists():
        nodeids.append(line)
# unique preserving order
seen=set(); nodeids=[n for n in nodeids if not (n in seen or seen.add(n))]

# AST source spans
spans={}
for py in (SRC/'tests').glob('*.py'):
    rel='tests/'+py.name
    try:
        tree=ast.parse(py.read_text())
    except SyntaxError:
        continue
    lines=py.read_text().splitlines()
    for cls in [None]+[n for n in tree.body if isinstance(n, ast.ClassDef)]:
        body = tree.body if cls is None else cls.body
        clsname = None if cls is None else cls.name
        for fn in body:
            if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
                key=(rel, clsname, fn.name)
                start=fn.lineno-1; end=getattr(fn,'end_lineno',fn.lineno)
                spans[key]='\n'.join(lines[start:end])

def base_parts(nodeid):
    parts=nodeid.split('::')
    file=parts[0]
    # strip parameter suffix from last part
    parts[-1]=re.sub(r'\[.*\]$', '', parts[-1])
    cls=None; fn=None
    if len(parts)>=3:
        cls=parts[-2]; fn=parts[-1]
    else:
        fn=parts[-1]
    return file, cls, fn, parts

def src_for(nodeid):
    file, cls, fn, parts=base_parts(nodeid)
    return spans.get((file, cls, fn)) or spans.get((file, None, fn)) or ''

file_default={
    'tests/test_action.py': ('Actions','atomic'),
    'tests/test_api.py': ('Embedded Execution API','integration'),
    'tests/test___init__.py': ('Top-Level API','atomic'),
    'tests/test___main__.py': ('Installable Surface','integration'),
    'tests/test_cmd_base.py': ('Command, Loader, Parser, Plugin, and Reporter APIs','integration'),
    'tests/test_cmdparse.py': ('Command, Loader, Parser, Plugin, and Reporter APIs','atomic'),
    'tests/test_dependency.py': ('Dependency State','atomic'),
    'tests/test_doit_cmd.py': ('Command, Loader, Parser, Plugin, and Reporter APIs','integration'),
    'tests/test_loader.py': ('Task Loading','integration'),
    'tests/test_plugin.py': ('Command, Loader, Parser, Plugin, and Reporter APIs','atomic'),
    'tests/test_task.py': ('Task Object API','atomic'),
    'tests/test_tools.py': ('Up-To-Date Helpers and Tools','atomic'),
}
# Files intentionally excluded as mostly private runner/control or exact command transcript tests.
exclude_files={
    'tests/test_cmd_help.py':'exact help text and task-help formatting are non-goals',
    'tests/test_cmd_completion.py':'shell completion exact script text is a non-goal',
    'tests/test_cmd_strace.py':'platform-specific strace details are non-goals',
    'tests/test_control.py':'internal dispatcher/control graph API not in candidate-visible spec',
    'tests/test_runner.py':'internal runner scheduling API and private worker methods are implementation-shaped',
    'tests/test_exceptions.py':'exact exception string/repr wording is non-goal',
}
# command modules mostly call private _execute or assert exact command output/storage internals
for f in ['test_cmd_clean.py','test_cmd_dumpdb.py','test_cmd_forget.py','test_cmd_ignore.py','test_cmd_info.py','test_cmd_list.py','test_cmd_resetdep.py','test_cmd_run.py']:
    exclude_files['tests/'+f]='direct command internals or exact command transcript/storage assertions'

exclude_name_patterns=[
    ('repr','repr format is source-only'),
    ('__repr__','repr format is source-only'),
    ('help','exact help text is non-goal'),
    ('usage','exact usage/help text is non-goal'),
    ('completion','shell completion exact script text is non-goal'),
    ('zsh','shell completion exact script text is non-goal'),
    ('strace','platform-specific strace details are non-goal'),
    ('pickle','pickle/internal serialization shape is source-only'),
    ('geststate','pickle/internal serialization shape is source-only'),
    ('safedict','pickle/internal serialization shape is source-only'),
]
private_tokens=['._', '.__dict__', '.__getstate__', '._CMDLINE_VARS', '._timeattr', '._key', '._remove_targets', '._action_instances', '._non_default_keys', '._execute', '._get', '._set', '._closed', '._run_', '._stop_running']
skipped=set()
skip_file=FILTER/'skipped_nodeids.txt'
if skip_file.exists():
    for s in skip_file.read_text().splitlines():
        s=s.strip()
        if not s:
            continue
        skipped.add(s if s.startswith('tests/') else 'tests/'+s)
dummy_passed=set()
dummy_pass_file=FILTER/'dummy_passed_nodeids.txt'
if dummy_pass_file.exists():
    for s in dummy_pass_file.read_text().splitlines():
        s=s.strip()
        if s:
            dummy_passed.add(s if s.startswith('tests/') else 'tests/'+s)

# Some public __str__ behavior is specified for InvalidCommand, but exact wording is excluded.
def classify(nodeid):
    file, cls, fn, parts=base_parts(nodeid)
    source=src_for(nodeid)
    low=(fn or '').lower()
    if file not in file_default and file not in exclude_files:
        return 'atomic','-','excluded','collected helper/non-test artifact, not a scoreable public behavior test'
    if file in exclude_files:
        return 'atomic','-','excluded',exclude_files[file]
    if nodeid in skipped:
        return 'atomic','-','excluded','reference run skipped this nodeid due optional/platform backend availability'
    if nodeid in dummy_passed:
        return 'atomic','-','excluded','dummy gate passed this nodeid; insufficient behavioral signal'
    if file == 'tests/test_action.py' and cls in {'TestWriter', 'TestCmd_print_process_output_line'}:
        return 'atomic','-','source-only','helper stream/private output reader behavior is not public API contract'
    if file == 'tests/test_action.py' and fn in {'test_str', 'test_unicode'}:
        return 'atomic','-','source-only','exact action string formatting is source-only'
    if file == 'tests/test_cmdparse.py' and cls in {'TestCmdOption_help_param', 'TestCmdOption_help_doc'}:
        return 'atomic','-','source-only','exact help formatting is non-goal'
    for pat, reason in exclude_name_patterns:
        if pat in low:
            return 'atomic','-','source-only',reason
    # private access/calls in function body, but allow dunder __main__ file name and normal magic method names in strings sparingly
    if any(tok in source for tok in private_tokens):
        return 'atomic','-','excluded','accesses or calls private implementation state/methods'
    if 'assertRaisesRegex' in source or 'pytest.raises' in source and 'match=' in source:
        return 'atomic','-','source-only','asserts exact exception message wording'
    if re.search(r'assert(In|Equal|Regex)\([^\n]*ERROR:|assert(In|Equal|Regex)\([^\n]*Traceback', source):
        return 'atomic','-','source-only','asserts exact error/traceback text'
    section, layer=file_default[file]
    # Refine by class/function names.
    full='::'.join(parts[1:]).lower()
    if 'error' in full or 'invalid' in full or 'fail' in full or 'missing' in full or 'not_exist' in full:
        section='Error Semantics'
    if file=='tests/test_task.py' and any(x in full for x in ['clean','teardown','actions','getargs','resultdep']):
        layer='integration'
    if file in {'tests/test_api.py','tests/test_doit_cmd.py','tests/test_loader.py'}:
        layer='integration'
    if file=='tests/test___main__.py':
        layer='system_e2e'
    if file=='tests/test_dependency.py' and any(x in full for x in ['filedependencies','uptodate','targets','ignore','save_']):
        layer='integration'
    if file=='tests/test_tools.py' and any(x in full for x in ['configchanged','timeout','checktimestamp','longrunning','interactive']):
        layer='integration'
    if file=='tests/test_task.py' and any(x in full for x in ['resultdep','clean','teardown']):
        section='Cross-View Invariants'
    if file=='tests/test_doit_cmd.py' and any(x in full for x in ['cmdline','config','plugin','subcommand']):
        section='Cross-View Invariants'
    return layer,section,'covered','upstream public behavior mapped to spec'

rows=[]; kept=[]; counts={'covered':0,'spec_gap':0,'source-only':0,'excluded':0}
for n in nodeids:
    layer,section,status,notes=classify(n)
    rows.append((n,layer,section,status,notes))
    counts[status]+=1
    if status=='covered': kept.append((n,layer,section))

# write spec_test_map
with (FILTER/'spec_test_map.md').open('w') as f:
    f.write('# Spec Test Map\n\n')
    f.write('filter/oracle_source: upstream_only\n\n')
    f.write('| test_nodeid | layer | spec_section | status | notes |\n')
    f.write('|---|---|---|---|---|\n')
    for n,layer,section,status,notes in rows:
        f.write(f'| `{n}` | {layer} | {section} | {status} | {notes} |\n')
    total=len(rows)
    f.write(f'\nTotal: {total} | kept (covered): {counts["covered"]} | spec_gap: {counts["spec_gap"]} | source-only: {counts["source-only"]} | excluded: {counts["excluded"]} | final scoreable: {counts["covered"]}\n')

(FILTER/'kept_nodeids.txt').write_text('\n'.join(n for n,_,_ in kept)+'\n')
# taxonomy jsonl
with (FILTER/'taxonomy.jsonl').open('w') as f:
    for n,layer,section in kept:
        p=n.split('::')
        stem=Path(p[0]).stem
        tail=[re.sub(r'\[.*\]$','',x) for x in p[1:]]
        key=stem + '::' + '.'.join(tail)
        f.write(json.dumps({'taxonomy_key':key,'layer':layer}, sort_keys=True)+'\n')
# score csv summary
layer_counts={}
section_counts={}
for _,layer,section in kept:
    layer_counts[layer]=layer_counts.get(layer,0)+1
    section_counts[section]=section_counts.get(section,0)+1
with (FILTER/'test_taxonomy_score.csv').open('w', newline='') as f:
    w=csv.writer(f)
    w.writerow(['metric','name','count'])
    w.writerow(['total','collected_functions',len(rows)])
    w.writerow(['total','kept_nodeids',len(kept)])
    for k,v in sorted(layer_counts.items()): w.writerow(['layer',k,v])
    for k,v in sorted(section_counts.items()): w.writerow(['spec_section',k,v])
print(json.dumps({'total':len(rows),'kept':len(kept),'counts':counts,'layers':layer_counts,'sections':section_counts}, indent=2, sort_keys=True))
