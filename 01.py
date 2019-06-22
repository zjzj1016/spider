import requests
str_ = '<a href="http://www.baidu.com/link?url=WBgZ_cq807A2EUKR_d85Y9ZGSSPHaDFhpLmZ62oZJVYqnTvFTKNPjCBDOVryDFaBzfgcBk1RACY9n17ZcBlB0UMwdL7JUQR7U3TmhGvSCgNoOvhpr3ZDd47M9Nnaj7sI" target="_blank" class="op-bk-polysemy-album op-se-listen-recommend" style="_height:121px">'
res = str_.split('=')[1]
print(res)
with open(res,'w',encoding='utf8') as f:
    f.write(res.text)