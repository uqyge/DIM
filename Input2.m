
%输入文件说明

%维数(ndim)， 总结点数(nnode)，  杆单元数目，   经典绳单元数(nelem_cable)，  Cluster绳单元数(nelem_1)
ndim=3;       nnode=12;        nelem_bar=2;      nelem_cable=3;            nelem_cluster=1;
mdof=ndim*nnode;

%Cluster矩阵（m*n）: m--cluster的根数; n--每根cluster含有的经典单元数目
cluster=[1,2,3,4,5,6];
mn=size(cluster);
m=mn(1,1);n=mn(1,2);

%单元编号分为三类：杆单元，经典绳单元，Cluster绳单元
ele_bar=[3,8;...
         5,9];

ele_cable=[2,10;...
           4,11;...
           6,12];

ele_cluster=[1,2;...
             2,3;...
             3,4;...
             4,5;...
             5,6;...
             6,7];

%单元材料参数（截面积，弹性模量，初应变，初应力）
a_cable=0.5e-4;
a_bar=2.8e-4;
a_cluster=1e-4;

e_bar=2e11;
e_cable=1e11;
e_cluster=1e11;

%节点坐标
nod=[0,0,0;...
    1,0.5,0;...
    2,0,0;...
    3,0.5,0;...
    4,0,0;...
    5,0.5,0;...
    6,0,0;...
    2,-1.5,0;...
    4,-1.5,0;...
    1,1.5,0;...
    3,1.5,0;...
    5,1.5,0];

%约束x向位移的节点，约束y向位移的节点，约束z向位移的节点
lrx=[1,7,8,9,10,11,12];
lry=[1,7,8,9,10,11,12];
lrz=[1,2,3,4,5,6,7,8,9,10,11,12];

xxx=size(lrx);yyy=size(lry);zzz=size(lrz);
nrx=xxx(1,2);nry=yyy(1,2);nrz=zzz(1,2);

%载荷信息，总加载步数，加载步长
f=zeros(mdof,1);
f(ndim*4-2,1)=0;

%===============================Initial====================================
nod_now=zeros(nnode,3);nod_delta=zeros(nnode,3);
dis0=zeros(mdof,1);dis1=zeros(mdof,1);delta_dis=zeros(mdof,1);
q=zeros(mdof,1);df=zeros(mdof,1);
kte_bar=zeros(6,6);kte_cable=zeros(6,6);kte_cluster=zeros(3*(n+1),3*(n+1));
Kt=zeros(mdof,mdof);





