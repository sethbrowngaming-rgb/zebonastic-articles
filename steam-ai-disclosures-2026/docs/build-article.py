import base64,re
D="/home/claude/steam-ai-disclosures-2026/"
def uri(n): return "data:image/png;base64,"+base64.b64encode(open(D+"images/"+n,"rb").read()).decode()
body=open(D+"docs/article-body.html").read()
m={"@@fig1@@":"fig1-disclosure-share-by-period.png","@@fig2@@":"fig2-disclosing-vs-other-counts.png","@@fig3@@":"fig3-disclosure-by-review-count.png","@@fig4@@":"fig4-uses-named-in-disclosures.png","@@table1@@":"table1-five-numbers.png","@@table2@@":"table2-explanations.png","@@table3@@":"table3-know-think-dont-know.png"}
# NOTE: in the body, @@fig3@@ is the uses chart?  Map by body order below.
body=body.replace("@@fig4@@","@@USES@@").replace("@@fig3@@","@@REVIEWS@@")
m2={"@@fig1@@":"fig1-disclosure-share-by-period.png","@@fig2@@":"fig2-disclosing-vs-other-counts.png","@@USES@@":"fig4-uses-named-in-disclosures.png","@@REVIEWS@@":"fig3-disclosure-by-review-count.png","@@table1@@":"table1-five-numbers.png","@@table2@@":"table2-explanations.png","@@table3@@":"table3-know-think-dont-know.png"}
for k,n in m2.items(): body=body.replace(k,uri(n))
assert "@@" not in body
css="""
*{box-sizing:border-box}body{margin:0;background:#fcfcfb;color:#0b0b0b;font:18px/1.6 Georgia,"Times New Roman",serif}
main{max-width:860px;margin:0 auto;padding:32px 20px 80px}
.kicker{font:700 13px/1 "Courier New",monospace;letter-spacing:.12em;color:#52514e;margin:0 0 14px}
h1{font:900 clamp(30px,5vw,46px)/1.08 Helvetica,Arial,sans-serif;margin:0 0 16px;border-bottom:6px solid #0b0b0b;padding-bottom:16px}
.dek{font:20px/1.45 Helvetica,Arial,sans-serif;border-left:8px solid #eb6834;padding-left:16px;margin:0 0 34px}
h2{font:800 24px/1.2 Helvetica,Arial,sans-serif;margin:44px 0 12px;padding:8px 12px;background:#0b0b0b;color:#fcfcfb}
h3{font:800 19px/1.3 Helvetica,Arial,sans-serif;margin:28px 0 8px;border-bottom:3px solid #eb6834;display:inline-block}
.tag{font:700 11px "Courier New",monospace;letter-spacing:.06em;border:2px solid #0b0b0b;padding:1px 6px;margin-right:6px;background:#fff;white-space:nowrap}
figure{margin:26px 0;border:3px solid #0b0b0b;padding:10px;background:#fff}figure img{display:block;width:100%;height:auto}
figcaption{font:14px/1.4 Helvetica,Arial,sans-serif;color:#52514e;margin-top:8px}
a{color:#0b0b0b;text-decoration-color:#eb6834;text-decoration-thickness:2px}a[href^="#s"]{font:12px Helvetica,Arial,sans-serif;vertical-align:super;line-height:0;margin-left:1px}
.sources{font:15px/1.5 Helvetica,Arial,sans-serif;padding-left:24px}.sources li{margin-bottom:8px;word-break:break-word}.srcnote{font:14px/1.4 Helvetica,Arial,sans-serif;color:#52514e}
li{margin-bottom:6px}
"""
html=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>What 49.9% Counts: Reading Steam\'s AI Disclosure Numbers | Zebonastic</title><meta name="description" content="49.9% of Steam releases in October 2026 carried an AI disclosure. What that flag measures, what it cannot, and the evidence behind it."><style>{css}</style></head><body><main>{body}</main></body></html>'
open(D+"steam-ai-disclosures.html","w").write(html)
print(len(html)//1024,"KB")
