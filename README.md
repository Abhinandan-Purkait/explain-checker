## explain-checker

This checks whether all the api-resources have a openAPI explain data or not.

### To make it work we need to run these.

- `git clone https://github.com/Abhinandan-Purkait/explain-checker.git`
- `chmod +x explain-checker.py`
- `cp explain-checker.py /usr/bin/`

### To run the code

- Run `explain-checker.py` from anywhere.

### Output

```
k8s@master-sh2:~$ explain-checker.py 
cs ------> T
cm ------> T
ep ------> T
ev ------> T
limits ------> T
ns ------> T
no ------> T
pvc ------> T
pv ------> T
po ------> T
rc ------> T
quota ------> T
sa ------> T
svc ------> T
crd ------> T
ds ------> T
deploy ------> T
rs ------> T
sts ------> T
hpa ------> T
cj ------> T
csr ------> T
cbackup ------> T
ccompletedbackup ------> T
cspc ------> T
cspi ------> T
crestore ------> T
cva ------> T
cvc ------> T
cvp ------> T
cvr ------> T
cv ------> T
--------------------> adoptopenebs -----------> X
--------------------> cscconfig -----------> X
--------------------> openebs -----------> X
ev ------> T
ing ------> T
lvmnode ------> T
lvmvol ------> T
ing ------> T
netpol ------> T
bdc ------> T
bd ------> T
--------------------> cast -----------> X
--------------------> cbkp -----------> X
--------------------> cbkpc -----------> X

```
