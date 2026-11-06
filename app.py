import argparse,hashlib,json,re,unittest
from pathlib import Path
def audit(lines):
 seen={};issues=[];valid=0
 for n,line in enumerate(lines,1):
  if not line.strip():continue
  try:r=json.loads(line)
  except json.JSONDecodeError:issues.append({'line':n,'kind':'invalid_json'});continue
  if not isinstance(r,dict)or not isinstance(r.get('prompt'),str)or not isinstance(r.get('completion'),str):issues.append({'line':n,'kind':'schema'});continue
  valid+=1;prompt=' '.join(r['prompt'].lower().split());key=hashlib.sha256(prompt.encode()).hexdigest();split=str(r.get('split','unspecified'))
  if key in seen:
   previous=seen[key];issues.append({'line':n,'kind':'split_leakage'if split!=previous[1]else'duplicate_prompt','first_line':previous[0]})
  else:seen[key]=(n,split)
  text=r['prompt']+' '+r['completion']
  if re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',text,re.I):issues.append({'line':n,'kind':'possible_email','detail':'value redacted'})
  if not prompt or not r['completion'].strip():issues.append({'line':n,'kind':'empty_text'})
  if len(text)>50000:issues.append({'line':n,'kind':'oversized_text','characters':len(text)})
 return {'valid_rows':valid,'unique_prompts':len(seen),'issues':issues,'method':'heuristic quality audit; not comprehensive PII detection'}
class Tests(unittest.TestCase):
 def test_leakage_and_redaction(self):
  rows=[json.dumps({'prompt':'Hello','completion':'x','split':'train'}),json.dumps({'prompt':' hello ','completion':'demo@example.test','split':'test'}),'broken'];r=audit(rows);k=[i['kind']for i in r['issues']];self.assertIn('split_leakage',k);self.assertIn('possible_email',k);self.assertIn('invalid_json',k);self.assertNotIn('demo@example.test',json.dumps(r))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('file',nargs='?');p.add_argument('--self-test',action='store_true');a=p.parse_args()
 if a.self_test:unittest.main(argv=['audit'])
 elif a.file:print(json.dumps(audit(Path(a.file).read_text(encoding='utf-8').splitlines()),indent=2))
 else:p.error('Supply dataset.jsonl')
